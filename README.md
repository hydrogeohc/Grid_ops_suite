# Grid Operations Suite

This repository provides a set of Python scripts and modules for simulating and integrating grid operations, AI suite integration, and best practices for MCP (Mission Critical Power) systems.

---
<details>
<summary>📁 Project Structure</summary>

.
├── .DS_Store
├── .gitignore
├── README.md
├── ai_suite_integration.py
├── grid_ops_client.py
├── grid_ops_host.py
├── grid_ops_research_example.py
├── grid_ops_server.py
├── mcp_best_practices.py
└── requirements.txt

</details>

- **ai_suite_integration.py**: Integrates AI suite functionalities with grid operations.
- **grid_ops_client.py**: Client-side script for interacting with the grid operations server.
- **grid_ops_host.py**: Host module for managing grid operations.
- **grid_ops_research_example.py**: Example script for research and experimentation.
- **grid_ops_server.py**: Server-side script for handling grid operations.
- **mcp_best_practices.py**: Contains best practices for Mission Critical Power systems.
- **requirements.txt**: Lists Python dependencies required to run the project.

---

## 🚀 Getting Started

### 1. Clone the Repository

git clone <git@github.com:hydrogeohc/MCP_implement_KH.git>
cd <MCP_implement_KH>


### 2. Set Up a Virtual Environment (Recommended)

python3 -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

### 3. Install Dependencies

pip install -r requirements.txt

---

## ⚡ Usage

### Run the Grid Operations Server

python grid_ops_server.py

### Run the Client

In a new terminal (with the virtual environment activated):

python grid_ops_client.py


### Other Scripts

- **Integrate AI suite:**
python ai_suite_integration.py

- **Experiment with research examples:**
python grid_ops_research_example.py

- **Review best practices:**
python mcp_best_practices.py

---

## 🛠️ Customization

- Edit the respective Python files to modify or extend functionalities as needed for your use case.
- Refer to comments and docstrings within each file for more details.

---

## 📝 Notes

- Ensure you have **Python 3.7 or higher** installed.
- For any issues or questions, please open an issue or contact the maintainer.