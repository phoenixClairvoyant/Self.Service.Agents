import dotenv
dotenv.load_dotenv() # our .env file defines OPENAI_API_KEY
from llama_agents import (
    AgentService,
    ControlPlaneServer,
    SimpleMessageQueue,
    AgentOrchestrator,
    LocalLauncher
)
from llama_index.core.agent import FunctionCallingAgentWorker
from llama_index.llms.openai import OpenAI
from llamaindex.src.tools.calculation_tool import multiplier, addition
import logging

# turn on logging so we can see the system working
logging.getLogger("llama_agents").setLevel(logging.INFO)




def single_agent()-> AgentService:
    # Set up the message queue and control plane
    message_queue = SimpleMessageQueue()
    control_plane = ControlPlaneServer(
        message_queue=message_queue,
        orchestrator=AgentOrchestrator(llm=OpenAI()),
    )
    #Define an agent worker
    agent = FunctionCallingAgentWorker.from_tools([multiplier, addition], llm=OpenAI()).as_agent()

    
    # Create an AgentService with the multiply tool
    agent_service = AgentService(
        agent=agent,
        message_queue=message_queue,
        description="Agent that can multiply and add numbers",
        service_name="calculator_agent"
    )
    # Launch the agent service
    launcher = LocalLauncher(services=[agent_service], control_plane=control_plane, message_queue=message_queue)
    return launcher

def multi_agent(message_queue: SimpleMessageQueue):
    #Define an agent worker
    agent = FunctionCallingAgentWorker.from_tools([multiplier, addition], llm=OpenAI()).as_agent()

    
    # Create an AgentService with the multiply tool
    agent_service = AgentService(
        agent=agent,
        message_queue=message_queue,
        description="Agent that can multiply and add numbers",
        service_name="calculator_agent",
        host="localhost",
        port=8003 )
    
    return agent_service