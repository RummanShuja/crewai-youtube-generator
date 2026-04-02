# CrewAI Multi-Agent YouTube Content Generator

This project demonstrates a simple **multi-agent AI system** built using CrewAI. It simulates a real-world workflow where multiple AI agents collaborate to complete a task — in this case, generating a YouTube script from a given topic.


## 🚀 Overview

Instead of relying on a single AI prompt, this project uses **multiple specialized agents** working together:

* **Research Agent** → gathers and simplifies information
* **Script Writer Agent** → converts research into a YouTube script

This mimics how real teams work — dividing responsibilities for better output. CrewAI enables building such structured workflows where agents collaborate step-by-step instead of handling everything in one prompt.


## 🧠 Key Concepts

* **Agents**: AI roles with specific responsibilities (researcher, writer)
* **Tasks**: Instructions assigned to agents
* **Crew**: A team of agents executing tasks
* **Process**: Defines execution order (sequential in this project)


## 📂 Project Structure

```text
├── agents.py   # Defines AI agents
├── tasks.py    # Defines tasks assigned to agents
├── tools.py    # (Optional) Add external tools
├── main.py     # Entry point to run the system
````


## ⚙️ How It Works

1.  User provides a topic.
2.  **Research agent**:
      * Explains the topic in 3 bullet points.
3.  **Script writer agent**:
      * Uses the research to generate a short YouTube script.
4.  Output is displayed in the terminal.

The workflow is **sequential**:
Research → Script Writing


## 🛠️ Tech Stack

  * Python
  * CrewAI
  * Ollama (Local LLM)
  * LLaMA 3.1


## 🔧 Setup Instructions

### 1\. Clone the repository

```bash
git clone <your-repo-link>
cd <project-folder>
```

### 2\. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate    # Windows
source venv/bin/activate # Mac/Linux
```

### 3\. Install dependencies

```bash
pip install crewai
```

### 4\. Install Ollama

Download from: [https://ollama.com](https://ollama.com)

Verify installation:

```bash
ollama --version
```

### 5\. Pull LLM model

```bash
ollama run llama3.1
```

-----

## ▶️ Run the Project

```bash
python main.py
```

-----

## 🧪 Example Input

```python
topic = "CrewAI Tutorial for Beginners"
```

## 📤 Example Output


**The agents successfully generate:**

  * 3 simplified bullet points explaining the research topic.
  * A complete, short YouTube script featuring:
      * An engaging Hook
      * A clear Explanation
      * A strong Outro



## 📌 Future Improvements

  * Add tools (web search, YouTube API)
  * Enable memory for agents
  * Add UI (Streamlit / Web app)
  * Use more advanced models
