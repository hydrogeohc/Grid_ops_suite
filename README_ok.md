# GridOps Suite

**Modular Grid Operations, Security, and Integration**

GridOps Suite is a modular Python framework designed for secure, scalable, and maintainable grid operations. It provides core grid operation tools, agent integration, workflow orchestration, and intentionally vulnerable demos for security testing and education. The project structure promotes clarity and extensibility, making it suitable for both production use and cybersecurity research.

---

## 🚩 Key Features

- **Modular Architecture:** Separates core grid logic, agent integration, workflows, and demos for maintainability and scalability.
- **Security Focus:** Includes dedicated security documentation, best practices, and intentionally vulnerable servers for testing and training.
- **Agent Integration:** Supports AI-driven agent orchestration and secure communication.
- **Educational Demos:** Provides vulnerable servers and attack clients for hands-on security learning.
- **Containerized Deployment:** Includes Docker support for streamlined setup and reproducibility.

---

## 📁 Project Structure
```
GRID_OPS_SUITE/
├── docs/security/           # Security analysis and testing guides
│   ├── ANALYSIS.md
│   └── TESTING.md
├── grid_ops/                # Core grid operation logic and agent integration
│   ├── __init__.py
│   ├── agent.py
│   ├── operations.py
│   ├── orchestrator.py
│   ├── security.py
│   └── server.py
├── insecure_demos/          # Vulnerable demo servers and attack clients
│   ├── a2a/
│   │   ├── a2a-attack-client.py
│   │   └── a2a-vulnerable-server.py
│   └── mcp/
│       ├── __init__.py
│       ├── attack-mcp-client.py
│       └── vuln-mcp.py
├── docker-compose.yml       # Container orchestration
├── Dockerfile               # Docker image definition
├── SECURITY.md              # Security policies and reporting
├── README.md
└── requirements.txt         # Python dependencies

```

- **grid_ops/**  
  Implements core grid operations, agent logic, security integration, and workflow orchestration  
  _(including `agent.py`, `operations.py`, `security.py`, `orchestrator.py`, and `server.py`)._

- **insecure_demos/**  
  Contains intentionally vulnerable demo servers and attack clients for security testing, organized into `a2a/` (agent-to-agent) and `mcp/` (multi-control protocol) subdirectories.

- **docs/security/**  
  Provides security analysis, audit reports, and testing instructions, such as `ANALYSIS.md` and `TESTING.md`.

- **Dockerfile** & **docker-compose.yml**  
  Enable containerized deployment and orchestration for development, testing, and production environments.

- **SECURITY.md**  
  Outlines security policies, best practices, and vulnerability reporting procedures.
---

## 🚀 Getting Started

1. **Clone the Repository**
git clone <git@github.com:hydrogeohc/Grid_ops_suite.git>
cd Grid_ops_suite

2. **Set Up a Virtual Environment (Recommended)**
python3 -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

3. **Install Dependencies**
pip install -r requirements.txt

---

## ⚡ Usage

- **Run the Grid Operations Server**
python -m grid_ops.server

- **Run the Orchestrator (Agent Workflow):
python -m grid_ops.orchestrator

- **Security Demos**
- Run insecure A2A demo server:
  ```
  python insecure_demos/a2a/a2a-vulnerable-server.py
  ```
- Test MCP vulnerabilities:
  ```
  python insecure_demos/mcp/attack-mcp-client.py
  ```

---

## 🛠️ Customization

- Modify or extend functionalities by editing Python files in the relevant module directories.
- Consult inline comments and docstrings for guidance.
- Refer to `docs/security/` for security best practices and analysis.

---

## 📝 Notes

- **Python 3.9 or higher** is required.
- For issues or questions, open a GitHub issue or contact the maintainer.
- Security documentation and audit reports are available in `docs/security/`.
- Follow `SECURITY.md` for vulnerability reporting procedures.

---

## 🛠️ Customization
- Extend or modify core grid operation logic in grid_ops/operations.py and related files.

