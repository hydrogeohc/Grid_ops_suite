# GridOps Suite: Modular Operations, Security, and Integration

This project is organized into modular directories to promote clarity, maintainability, and scalability. Core grid operations are handled in the grid_ops module, while adk_integration manages agent and security integration. The a2a_workflows folder contains orchestration logic for agent-to-agent workflows. For educational and testing purposes, the insecure_demos directory provides intentionally vulnerable A2A and MCP servers alongside attack clients. Comprehensive security documentation and analysis are available in the docs/security folder. Deployment and environment configuration are streamlined with docker-compose.yml, Dockerfile, and requirements.txt, and security policies are outlined in SECURITY.md. This structure ensures a robust foundation for both development and secure operations.

---

## 📁 Project Structure
```
project-root/
├── grid_ops/
│ ├── init.py
│ ├── server.py
│ └── operations.py
├── adk_integration/
│ ├── init.py
│ ├── agent.py
│ └── security.py
├── a2a_workflows/
│ ├── init.py
│ └── orchestrator.py
├── insecure_demos/
│ ├── a2a/
│ │ ├── a2a-vulnerable-server.py
│ │ └── a2a-attack-client.py
│ └── mcp/
│ ├── vuln-mcp.py
│ └── attack-mcp-client.py
├── docs/
│ └── security/
│ ├── ANALYSIS.md
│ └── TESTING.md
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── SECURITY.md
```


grid_ops/

Contains core logic for grid operations.

__init__.py: Initializes the grid operations module.

server.py: Exposes grid operation tools and server endpoints.

operations.py: Implements the main grid operation functions (e.g., forecasting, optimization).

adk_integration/

Manages integration with AI-driven agents and security protocols.

__init__.py: Initializes the ADK integration module.

agent.py: Defines agent setup and communication logic.

security.py: Handles secure connections and secret management.

a2a_workflows/

Implements agent-to-agent workflow orchestration.

__init__.py: Initializes the A2A workflows module.

orchestrator.py: Coordinates multi-agent interactions and tasks.

insecure_demos/

Provides intentionally vulnerable demo servers and attack clients for security testing and education.

a2a/

a2a-vulnerable-server.py: Example of a vulnerable A2A server (e.g., SQL injection).

a2a-attack-client.py: Demonstrates attacks against the vulnerable server.

mcp/

vuln-mcp.py: Example of a vulnerable MCP server (e.g., remote code execution).

attack-mcp-client.py: Demonstrates attacks against the vulnerable MCP server.

docs/security/

Contains security documentation and testing guides.

ANALYSIS.md: Security analysis and best practices.

TESTING.md: Instructions for testing vulnerabilities and secure patterns.


---

## 🚀 Getting Started

### 1. Clone the Repository

git clone git@github.com:hydrogeohc/MCP_implement_Grid.git
cd MCP_implement_Grid

### 2. Set Up a Virtual Environment (Recommended)

python3 -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate


### 3. Install Dependencies

pip install -r requirements.txt


---

## ⚡ Usage

### Run the Grid Operations Server

python -m grid_ops.server


### Run the Client

In a new terminal (with the virtual environment activated):

python grid_ops_client.py


### Security Demos

Run insecure A2A demo:

python insecure_demos/a2a/a2a-vulnerable-server.py

Test MCP vulnerabilities:

python insecure_demos/mcp/attack-mcp-client.py


---

## 🛠️ Customization

- Edit the respective Python files in the module directories to modify or extend functionalities.
- Refer to comments and docstrings within each file for more details.
- See `docs/security/` for security guidance and best practices.

---

## 📝 Notes

- Requires **Python 3.9 or higher** for full functionality.
- For any issues or questions, please open an issue or contact the maintainer.
- Security audit reports and documentation are in `docs/security/`.
- Use `SECURITY.md` for vulnerability reporting procedures.