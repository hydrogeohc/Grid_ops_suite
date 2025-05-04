def handle_operation(tool_name, params):
    """
    Dispatches the requested grid operation.
    """
    if tool_name == "load_forecast":
        return load_forecast(params)
    elif tool_name == "grid_optimize":
        return grid_optimize(params)
    else:
        return {"error": f"Unknown tool: {tool_name}"}


def load_forecast(params):
    """
    Dummy implementation of load forecasting.
    """
    timeframe = params.get("timeframe", "24h")
    resolution = params.get("resolution", 1)
    # Simulate a forecast
    forecast = [100 + i * resolution for i in range(24)]
    return {
        "timeframe": timeframe,
        "resolution": resolution,
        "forecast": forecast
    }


def grid_optimize(params):
    """
    Dummy implementation of grid optimization.
    """
    topology = params.get("topology", {})
    constraints = params.get("constraints", [])
    # Simulate optimization result
    optimized = {"topology": topology, "constraints": constraints, "status": "optimized"}
    return optimized
