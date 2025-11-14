# AI Coding Agent (Gemini Flash)

An **AI-powered coding assistant** built on **Google Gemini Flash**, designed to help with everyday software development tasks directly inside your working directory.

The agent uses Gemini’s **function-calling** system to safely inspect files, read content, write code, and execute Python—while remaining fully sandboxed for security.

---

## 🚀 Features

### ✔ Intelligent Coding Assistance
- Responds to natural language coding requests  
- Writes, edits, and refactors Python code  
- Generates new files or updates existing ones  
- Can run Python scripts and return their output  

### ✔ Secure Tool Access
The agent exposes four controlled tools:

| Tool                | Description                                 |
|--------------------|---------------------------------------------|
| `get_files_info`   | Lists files & directories with metadata      |
| `get_file_content` | Reads file contents safely                   |
| `write_file`       | Writes & overwrites files within the working directory |
| `run_python_file`  | Executes Python scripts in a sandbox         |

### ✔ Sandboxed Execution
To prevent security issues, the agent is **restricted to the current working directory**.  
It cannot access arbitrary system files or navigate upward in the filesystem.

### ✔ Multi-Step Reasoning
The agent can:
- Read a file  
- Analyze it  
- Write edits  
- Run the script  
- Inspect output  
…all in one iterative reasoning loop powered by function-calling.

---

## 🧠 How It Works

The agent follows a strict message loop:

1. **User sends a request**
2. **Gemini Flash** returns:
   - natural language answers, *or*
   - one or more structured `function_call` objects
3. The Python runtime executes the requested functions
4. Results are returned to Gemini as `function_response`
5. Gemini continues reasoning with full context until finished

This architecture allows Gemini to behave like a lightweight, local ReAct agent.

---

## 📂 Project Structure
aiagent/
│
├── README.md               # Project documentation
├── main.py                 # Core agent loop (Gemini orchestration)
├── config.py               # Model config / runtime parameters
├── call_function.py        # Function-call dispatching
│
├── functions/              # Toolbox for agent actions
│   ├── file_tools.py       # File reading/writing helpers
│   └── python_runner.py    # Safe Python execution logic
│
├── calculator/             # Additional utilities / example code
│
├── tests.py                # Test coverage for tools and logic
│
├── pyproject.toml          # Build system metadata
├── pyvenv.cfg              # Virtual environment configuration
├── bin/                    # Virtual environment scripts
├── lib/                    # Virtual environment libraries
├── include/                # Virtual environment headers

---

## 🧩 Example Usage

**User Prompt:**

> "My calculator is outputting wrong results. Help me fix my calculator and show me the diff."

Agent behavior:

1. Reads `main.py`
2. Writes a refactored version
3. Produces a diff
4. Displays the result

---