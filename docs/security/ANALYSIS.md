# Security Analysis

## Insecure Patterns Demonstrated

- **SQL Injection:** The A2A demo server is vulnerable to SQL injection via direct string formatting in SQL queries.
- **Remote Code Execution (RCE):** The MCP demo server executes arbitrary code received over the network.
- **No Authentication:** Both demo servers lack authentication and authorization checks.

## Recommendations

- Always use parameterized queries for database access.
- Never use `exec` or `eval` on untrusted input.
- Implement authentication and authorization for all endpoints.
- Use secure channels (e.g., HTTPS) for communication.
