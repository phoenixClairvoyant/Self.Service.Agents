import os
import numpy as np
from dotenv import load_dotenv
from trulens_eval import Feedback,TruLlama,FeedbackMode
from trulens_eval.feedback import GroundTruthAgreement
from llama_index.core.tools import QueryEngineTool
from llama_index.core import (SimpleDirectoryReader, VectorStoreIndex, Settings)
from trulens.core import TruSession
from llama_index.llms.openai import OpenAI
from llama_index.llms.gemini import Gemini

from llama_index.core import SummaryIndex
from llama_index.core import VectorStoreIndex
from llama_index.core import StorageContext
from llama_index.core.tools import QueryEngineTool

from llama_index.core.query_engine import RouterQueryEngine
from llama_index.core.selectors import LLMSingleSelector, LLMMultiSelector
from llama_index.core.selectors import (
    PydanticMultiSelector,
    PydanticSingleSelector,
)

from trulens_eval import OpenAI as fOpenAI


class RagTool(QueryEngineTool):
    def __init__(self, data_files: list=None,
                 data_folder: str = "datastore/platform_wikis/docs/architectural_decision_records",
                 use_gemini: bool = False,
                 app_id:str="App_1") -> None:
        
        Settings.chunk_size = 1024
        Settings.chunk_overlap = 16
        Settings.llm = Gemini() if use_gemini else OpenAI()
        documents = SimpleDirectoryReader(input_dir=data_folder, input_files=data_files).load_data()
        provider = fOpenAI()
        
        # Old implementtion
        index = VectorStoreIndex.from_documents(documents)
        query_engine = index.as_query_engine(similarity_top_k=3)
        
        # New implementation
        # initialize storage context (by default it's in-memory)
        nodes = Settings.node_parser.get_nodes_from_documents(documents)
        storage_context = StorageContext.from_defaults()
        storage_context.docstore.add_documents(nodes)
        summary_index = SummaryIndex(nodes, storage_context=storage_context)
        vector_index = VectorStoreIndex(nodes, storage_context=storage_context)
        
        list_query_engine = summary_index.as_query_engine(response_mode="tree_summarize", use_async=True)
        vector_query_engine = vector_index.as_query_engine()
        

        self.budgetor = QueryEngineTool.from_defaults(
            query_engine,
            name="canadian_budget_2023",
            description="A RAG engine with some basic facts about the 2023 Canadian federal budget.",
        )
        
        self.platform_wiki = QueryEngineTool.from_defaults(
            query_engine,
            name="platform_wiki",
            description="A RAG engine with information on platform wikis. These include architecture decision records, data management, operations, databricks and many others.",
        )
        self.list_tool = QueryEngineTool.from_defaults(
        query_engine=list_query_engine,
            name="canadian_budget_2023",
            description="A RAG engine with some basic facts about the 2023 Canadian federal budget.",
        )

        self.vector_tool = QueryEngineTool.from_defaults(
            query_engine=vector_query_engine,
            name="platform_wiki",
            description="A RAG engine with information on platform wikis. These include architecture decision records, data management, operations, databricks and many others.",
        )
    
        self.router_engine = RouterQueryEngine(
            selector=LLMSingleSelector.from_defaults(),
            query_engine_tools=[self.list_tool, self.vector_tool],)
     
        
        
        