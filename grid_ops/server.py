from .operations import handle_operation

class GridOpsServer:
    def list_tools(self):
        return {
            "load_forecast": {
                "description": "Predict power demand using historical data",
                "parameters": {
                    "timeframe": "string",
                    "resolution": "number"
                }
            },
            "grid_optimize": {
                "description": "Optimize power distribution",
                "parameters": {
                    "topology": "object",
                    "constraints": "array"
                }
            }
        }

    def call_tool(self, tool_name, params):
        return handle_operation(tool_name, params)

if __name__ == "__main__":
    server = GridOpsServer()
    print("Available tools:")
    for name, info in server.list_tools().items():
        print(f" - {name}: {info['description']}")
    tool = input("Enter tool name: ")
    params = input("Enter params as a Python dict: ")
    try:
        params_dict = eval(params)
    except Exception:
        params_dict = {}
    print("Result:", server.call_tool(tool, params_dict))
