import asyncio
from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

async def create_grid_agent():
    tools, exit_stack = await MCPToolset.from_server(
        connection_params=StdioServerParameters(
            command='python',
            args=["-m", "grid_ops.server"]
        )
    )
    
    return LlmAgent(
        model='gemini-2.0-flash',
        name='grid_operator',
        instruction='Power grid optimization expert using MCP tools',
        tools=tools
    ), exit_stack
