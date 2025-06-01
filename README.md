# Tool Agent

A simple agent built using the Google Agent Development Kit (ADK). This agent is designed to be a helpful assistant and currently includes a custom tool to get the current time.

## Description

The `tool_agent` demonstrates the basic setup of an agent using the `google.adk.agents.Agent` class. It is configured to use the `gemini-2.0-flash-001` model and is equipped with a custom tool.

The primary purpose of this example is to show how to:
- Define an agent with a specific model, name, description, and instructions.
- Create and integrate custom tools for the agent to use.

## Features

- **Gemini Powered**: Utilizes the `gemini-2.0-flash-001` model for its conversational capabilities.
- **Custom Tool**: Includes a `get_current_time` tool that allows the agent to fetch and return the current date and time.
- **Extensible**: Designed to be easily extended with more tools. The agent code (`agent.py`) also shows an example of the built-in `google_search` tool, though there are considerations for mixing tool types (see "Tools" section).

## Project Structure

```
Tool Agent/
├── tool_agent/
│   ├── __init__.py
│   └── agent.py
└── README.md
```

- `tool_agent/__init__.py`: Makes the `agent` module available for import.
- `tool_agent/agent.py`: Contains the agent definition and the custom tool logic.

## Requirements

- Python 3.9+
- `google-adk` library
- `google-genai` library

## Setup and Installation

1.  **Clone the repository (if applicable):**
    If this project were hosted on a version control system like Git, you would clone it:
    ```bash
    git clone <repository-url>
    cd Tool-Agent
    ```

2.  **Create and configure the environment:**

    a.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
    ```

    b.  **Create a `.env` file:**
        In the root directory of the project (e.g., `/Users/ebubeimoh/Documents/AI Development Kit/Tool Agent/.env`), create a file named `.env`. This file will store your environment variables, such as your API key.

        Add your Google API key to the `.env` file like this:
        ```env
        GOOGLE_API_KEY="YOUR_API_KEY_HERE"
    ```

3.  **Install dependencies:**
    You'll need the `google-adk` package.
    ```bash
    pip install google-adk google-genai
    ```

## Usage

The `agent.py` file defines `root_agent`. You can interact with this agent using the `adk` command-line interface.

1.  **Activate the virtual environment** (if you haven't already):
    ```bash
    source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
    ```


2.  **Run the agent using the ADK CLI:**
    Once the virtual environment is activated and dependencies are installed, you can start a chat session with your agent using the following command in your terminal:
    ```bash
    adk run tool_agent
    ```
    This will load your `root_agent` and allow you to interact with it directly. For example, you can try asking:
    ```
    What is the current time?
    ```
    The agent should then use its `get_current_time` tool to respond.


## Tools

The agent is currently configured with the following tool:

-   **`get_current_time(format: str)`**:
    -   **Description**: Returns the current time.
    -   **Output**: A dictionary containing the current time formatted as `YYYY-MM-DD HH:MM:SS`. For example: `{"current time": "2023-10-27 14:30:00"}`.

The agent's instruction prompt explicitly mentions this tool, guiding the LLM to use it when appropriate.