from google.adk.agents import Agent
from google.adk.tools import google_search

from datetime import datetime

# Tool to get the current time
def get_current_time() -> dict:
    """
    Returns the current time in YYYY-MM-DD HH:MM:SS format.
    """
    return {
        "current time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

# Agent definition
root_agent = Agent(
    model='gemini-2.0-flash-001',
    name='tool_agent',
    description='You are a helpful assistant.',
    instruction="""
                You can use the folllowing tools:
                - get_current_time
                """,
    # tools=[google_search],
    tools=[get_current_time],
)
