
from mcp_use import MCPAgent, MCPClient
from contextlib import contextmanager
from langchain_ollama.chat_models import ChatOllama
from typing import Tuple, Generator

SERVER_PATH = "mcp_server.py"

CONFIG = {
    "mcpServers": {
        "base": {
            "command": "uvicorn",
            "args": ["run", SERVER_PATH]
        }
    }
}

@contextmanager
def mcp_client_context() -> Generator[Tuple[MCPClient, MCPAgent], None, None]:
    llm = ChatOllama(model="qwen3:8b", base_url="http://localhost:11434")
    client = MCPClient.from_dict(CONFIG)
    agent = MCPAgent(llm=llm, client=client, max_steps=20)
    try:
        yield client, agent
    finally:
        agent.close()
        client.close_session()
        



    