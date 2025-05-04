# Grid Operations Suite

This repository provides a set of Python scripts and modules for simulating and integrating grid operations, AI suite integration, and best practices for Model Context Protocol (MCP) systems.

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


Other notable scripts and files:
- **ai_suite_integration.py**: Integrates AI suite functionalities with grid operations.
- **grid_ops_client.py**: Client-side script for interacting with the grid operations server.
- **grid_ops_host.py**: Host module for managing grid operations.
- **grid_ops_research_example.py**: Example script for research and experimentation.
- **grid_ops_server.py**: Server-side script for handling grid operations.
- **mcp_best_practices.py**: Contains best practices for MCP systems.
- **mcp_troubleshooting**: General guidance for MCP troubleshooting.

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


### Other Scripts

- **Integrate AI suite:**  
  `python ai_suite_integration.py`
- **Experiment with research examples:**  
  `python grid_ops_research_example.py`
- **Review best practices:**  
  `python mcp_best_practices.py`

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