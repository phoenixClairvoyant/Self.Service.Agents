import os
# import numpy as np
# from crewai_tools import tool
from dotenv import load_dotenv
# from llama_index.core.tools import QueryEngineTool,ToolMetadata
from llama_cloud import PydanticProgramMode
from llama_index.core import (
    SimpleDirectoryReader, VectorStoreIndex, Settings)

from crewai_tools import LlamaIndexTool
from llama_index.llms.openai import OpenAI
from qdrant_client import AsyncQdrantClient, QdrantClient
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.core.node_parser import SemanticSplitterNodeParser, SentenceSplitter

load_dotenv()


Settings.chunk_size = 1024
Settings.chunk_overlap = 128
Settings.llm = OpenAI(model="gpt-4o-mini", temperature=0, pydantic_program_mode=PydanticProgramMode.OPENAI,
                      default_headers={"api-key": os.environ["OPENAI_API_KEY"]})

# host points to qdrant in docker-compose.yml
client = QdrantClient(host="qdrant", port=6333)
aclient = AsyncQdrantClient(host="qdrant", port=6333)
vector_store = QdrantVectorStore(
    collection_name="explore_adrs",
    client=client,
    aclient=aclient,
)

vector_store_index = VectorStoreIndex.from_vector_store(
    vector_store=vector_store,
    embed_model=OpenAIEmbedding(model_name="text-embedding-3-small"),
)

# ensure the index exists
if not client.collection_exists("explore_adrs"):
    documents = SimpleDirectoryReader(
        input_dir="./tools/datastore/architectural_decision_records").load_data()
    # Double pass chunking
    first_node_parser = SemanticSplitterNodeParser(
        embed_model=OpenAIEmbedding(model_name="text-embedding-3-small"),
    )
    second_node_parser = SentenceSplitter(Settings.chunk_size, Settings.chunk_overlap)
    nodes = first_node_parser(documents)

    # Second pass chunking ensures that the nodes are not too large
    nodes = second_node_parser(nodes)
    vector_store_index.insert_nodes(nodes)


vector_query_engine = vector_store_index.as_query_engine()
query_tool = LlamaIndexTool.from_query_engine(
    query_engine=vector_query_engine,
    name="Rag Tool",
    description="Use this tool to reference the company's knowledge base. These include architecture decision records, data management standards and many others.",
)
