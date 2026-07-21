from smolagents import ToolCallingAgent, tool, OpenAIModel, WebSearchTool
from datetime import datetime
from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv()

m_api = os.environ.get("API_KEY")
tav_api = os.environ.get("tav_key")

client = TavilyClient(tav_api)  # api calling to tavily

model = OpenAIModel(
    model_id="openai/gpt-oss-20b:free",
    api_base="https://openrouter.ai/api/v1",
    api_key=m_api,
)


@tool
def search_web(query: str) -> str:
    """
    Searches the web using tavily and returns relevant results
    Args:
      query:The search query String
    """
    response = client.search(query, max_results=5)
    result = response.get("results", [])

    formatted = ""
    for r in result:
        formatted += f"title: {r['title']}\nURL: {r['url']}\nContent: {r['content']}\n"
    return formatted


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
    tools=[WebSearchTool(), calculate_sum, format_report, search_web],
    model=model,
)

result = agent.run(
    "What are the key differences between Groq and OpenAI for running LLMs?"
)
print(result)
