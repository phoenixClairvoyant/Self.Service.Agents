import os
import numpy as np
from dotenv import load_dotenv
from trulens_eval import Feedback,TruLlama,FeedbackMode
from trulens_eval.feedback import GroundTruthAgreement
from llama_index.core import (
    SimpleDirectoryReader, VectorStoreIndex, Settings, SummaryIndex,
    StorageContext, QueryEngineTool, RouterQueryEngine
)
from llama_index.core.selectors import LLMSingleSelector
from llama_index.llms.openai import OpenAI
from llama_index.llms.gemini import Gemini
from trulens_eval import OpenAI as fOpenAI

class RagTool(QueryEngineTool):
    def __init__(self, data_files=None,
                 data_folder="datastore/platform_wikis/docs/architectural_decision_records",
                 use_gemini=False,
                 app_id="App_1"):
        
        Settings.chunk_size = 1024
        Settings.chunk_overlap = 16
        Settings.llm = Gemini() if use_gemini else OpenAI()
        
        documents = SimpleDirectoryReader(input_dir=data_folder, input_files=data_files).load_data()
        nodes = Settings.node_parser.get_nodes_from_documents(documents)
        
        storage_context = StorageContext.from_defaults()
        storage_context.docstore.add_documents(nodes)
        
        summary_index = SummaryIndex(nodes, storage_context=storage_context)
        vector_index = VectorStoreIndex(nodes, storage_context=storage_context)
        
        list_query_engine = summary_index.as_query_engine(response_mode="tree_summarize", use_async=True)
        vector_query_engine = vector_index.as_query_engine()
        
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
            query_engine_tools=[self.list_tool, self.vector_tool],
        )

