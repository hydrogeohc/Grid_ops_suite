def handle_operation(tool_name, params):
    if tool_name == "load_forecast":
        return load_forecast(params)
    elif tool_name == "grid_optimize":
        return grid_optimize(params)
    else:
        return {"error": f"Unknown tool: {tool_name}"}

def load_forecast(params):
    timeframe = params.get("timeframe", "24h")
    resolution = params.get("resolution", 1)
    forecast = [100 + i * resolution for i in range(24)]
    return {
        "timeframe": timeframe,
        "resolution": resolution,
        "forecast": forecast
    }

def grid_optimize(params):
    topology = params.get("topology", {})
    constraints = params.get("constraints", [])
    return {
        "topology": topology,
        "constraints": constraints,
        "status": "optimized"
    }