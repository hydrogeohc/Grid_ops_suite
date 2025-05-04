from google.adk.workflows import ParallelWorkflow
from adk_integration.agent import create_grid_agent

class GridWorkflow:
    def __init__(self):
        self.workflow = ParallelWorkflow(
            agents={
                'forecaster': self._load_forecasting_agent(),
                'optimizer': self._grid_optimization_agent(),
                'safety': self._grid_safety_agent()
            }
        )
    
    async def handle_grid_event(self, event):
        return await self.workflow.execute({
            'forecaster': {'task': 'predict_demand', 'params': event},
            'optimizer': {'task': 'optimize_grid', 'depends_on': ['forecaster']},
            'safety': {'task': 'validate_operations', 'depends_on': ['optimizer']}
        })
    
    async def _load_forecasting_agent(self):
        agent, _ = await create_grid_agent()
        return agent
    
    async def _grid_optimization_agent(self):
        agent, _ = await create_grid_agent()
        return agent
    
    async def _grid_safety_agent(self):
        agent, _ = await create_grid_agent()
        return agent
