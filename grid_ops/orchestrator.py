import asyncio
from google.adk.agents import ParallelAgent, Agent
from .agent import create_grid_agent  # Relative import for package
from .operations import handle_operation  # Import operations if needed

class GridWorkflow:
    def __init__(self):
        self.workflow = None
        self.agents_initialized = False

    async def initialize_agents(self):
        """Async initialization of all agents"""
        forecaster, _ = await create_grid_agent()
        optimizer, _ = await create_grid_agent()
        safety, _ = await create_grid_agent()
        
        self.workflow = ParallelAgent(
            name="grid_workflow",
            sub_agents=[
                Agent(name="forecaster", agent=forecaster),
                Agent(name="optimizer", agent=optimizer),
                Agent(name="safety", agent=safety)
            ]
        )
        self.agents_initialized = True

    async def run_workflow(self, event_data):
        """Execute workflow with sample data"""
        if not self.agents_initialized:
            await self.initialize_agents()
            
        print("🟢 Starting grid optimization workflow...")
        result = await self.workflow.execute({
            "event": event_data,
            "tools": ["load_forecast", "grid_optimize"]
        })
        print("🔵 Workflow completed with result:", result)
        return result

if __name__ == "__main__":
     async def main():
        workflow = GridWorkflow()
        event = {
            "timeframe": "24h",
            "resolution": 1,
            "topology": {"nodes": 5, "connections": 10},
            "constraints": ["max_load=120"]
        }
        result = await workflow.handle_grid_event(event)
        print("Workflow result:", result)

        asyncio.run(main())