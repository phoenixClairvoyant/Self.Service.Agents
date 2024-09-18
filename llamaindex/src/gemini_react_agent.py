import os
import json
from typing import Sequence, List
from dotenv import load_dotenv
from llama_index.llms.gemini import Gemini
from llama_index.llms.openai import OpenAI
from llama_index.core.llms import ChatMessage
from llama_index.core.tools import BaseTool, FunctionTool
from openai.types.chat import ChatCompletionMessageToolCall

import nest_asyncio

from tools.calculation_tool import multiplier, addition
from tools.rag_tool import RagTool

nest_asyncio.apply()

load_dotenv()
os.environ['GEMINI_API_KEY'] = os.getenv('GEMINI_API_KEY')
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv('GEMINI_API_KEY')
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

rag_tool = RagTool(data_folder="datastore/platform_wikis/docs/architectural_decision_records", use_gemini=True)

class GeminiAiAgent:
    def __init__(
        self,
        tools: Sequence[BaseTool] = [],
        llm: Gemini = Gemini(model="gemini-pro", temperature=0),
        chat_history: List[ChatMessage] = [],
    ) -> None:
        self._llm = llm
        self._tools = {tool.metadata.name: tool for tool in tools}
        self._chat_history = chat_history

    def reset(self) -> None:
        self._chat_history = []

    def chat(self, message: str) -> str:
        chat_history = self._chat_history
        chat_history.append(ChatMessage(role="user", content=message))
        tools = [
            tool.metadata.to_openai_tool() for _, tool in self._tools.items()
        ]

        ai_message = self._llm.chat(chat_history, tools=tools).message
        additional_kwargs = ai_message.additional_kwargs
        chat_history.append(ai_message)

        tool_calls = additional_kwargs.get("tool_calls", None)
        # parallel function calling is now supported
        if tool_calls is not None:
            for tool_call in tool_calls:
                function_message = self._call_function(tool_call)
                chat_history.append(function_message)
                ai_message = self._llm.chat(chat_history).message
                chat_history.append(ai_message)

        return ai_message.content

    def _call_function(
        self, tool_call: ChatCompletionMessageToolCall
    ) -> ChatMessage:
        id_ = tool_call.id
        function_call = tool_call.function
        tool = self._tools[function_call.name]
        output = tool(**json.loads(function_call.arguments))
        return ChatMessage(
            name=function_call.name,
            content=str(output),
            role="tool",
            additional_kwargs={
                "tool_call_id": id_,
                "name": function_call.name,
            },
        )
def rag_docs(query: str):
    # load the documents and create the index
    agent = GeminiAiAgent(
    [multiplier, addition, rag_tool.router_engine])
    response = agent.chat(query)
    return response # response