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
project-root/
├── grid_ops/ # Core grid operation logic (server, operations)
├── adk_integration/ # Agent and security integration modules
├── a2a_workflows/ # Agent-to-agent workflow orchestration
├── insecure_demos/ # Vulnerable servers and attack clients for demos
│ ├── a2a/
│ └── mcp/
├── docs/
│ └── security/ # Security analysis and testing guides
├── docker-compose.yml # Container orchestration
├── Dockerfile # Docker image definition
├── requirements.txt # Python dependencies
└── SECURITY.md # Security policies and reporting
```

- **grid_ops/**: Implements core grid operations, including forecasting and optimization logic.
- **adk_integration/**: Manages AI agent setup, communication, and security protocols.
- **a2a_workflows/**: Coordinates multi-agent workflows and task orchestration.
- **insecure_demos/**: Contains intentionally vulnerable A2A and MCP servers and attack clients for security testing.
- **docs/security/**: Provides security analysis, best practices, and testing instructions.
- **Docker/Docker Compose**: Enables containerized deployment for development and production.

---

## 🚀 Getting Started

1. **Clone the Repository**
git clone <git@github.com:hydrogeohc/Grid_ops_suite.git>
cd Grid_ops_suite

text

2. **Set Up a Virtual Environment (Recommended)**
python3 -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

text

3. **Install Dependencies**
pip install -r requirements.txt

text

---

## ⚡ Usage

- **Run the Grid Operations Server**
python -m grid_ops.server

text

- **Run the Client**
python grid_ops_client.py

text

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



