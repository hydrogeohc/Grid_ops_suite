# Security Testing

## Testing SQL Injection

1. Run the vulnerable A2A server:
python insecure_demos/a2a/a2a-vulnerable-server.py

2. Run the attack client:
python insecure_demos/a2a/a2a-attack-client.py

3. Observe the server output and database state.

## Testing Remote Code Execution

1. Run the vulnerable MCP server:
python insecure_demos/mcp/vuln-mcp.py

2. Run the attack client:
python insecure_demos/mcp/attack-mcp-client.py

3. Check for the presence of `hacked.txt` on the server.