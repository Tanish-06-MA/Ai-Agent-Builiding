from smolagents import ToolCallingAgent, tool, OpenAIModel, WebSearchTool
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

api = os.environ.get("API_KEY")

model = OpenAIModel(
    model_id="openai/gpt-oss-20b:free",
    api_base="https://openrouter.ai/api/v1",
    api_key=api,
)


@tool
def calculate_sum(a: int, b: int) -> int:
    """
    Adds two numbers

    Args:
        a:First Number
        b:Second Number

    Returns: sum of two numbers
    """
    return a + b


@tool
def get_date() -> str:
    """Tells user about todays date"""
    return str(datetime.today())


@tool
def format_report(date: str, sum: int) -> str:
    """
    Formats the ans in a proper String format

    Args:
        date: output of get_date tool
        sum: output of calculate_sum tool

    Returns:
        A formatted report containing the date and the sum.
    """
    return f"Date :{date}\nSum :{sum}"


agent = ToolCallingAgent(
    tools=[WebSearchTool(), calculate_sum, get_date, format_report], model=model
)

result = agent.run("What is 45 + 78, and what is today's date?")
print(result)
