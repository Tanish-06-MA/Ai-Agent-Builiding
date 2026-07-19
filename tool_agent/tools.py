from smolagents import GradioUI, CodeAgent, OpenAIModel, WebSearchTool, tool
from dotenv import load_dotenv
from datetime import date
import os

load_dotenv()

api = os.environ.get("API_KEY")

model = OpenAIModel(
    model_id="openai/gpt-oss-20b:free",
    api_base="https://openrouter.ai/api/v1",
    api_key=api,
)


@tool
def get_current_date() -> str:
    """Returns todays date"""
    return str(date.today())


agent = CodeAgent(tools=[WebSearchTool(), get_current_date], model=model)

result = agent.run("Fetch the data of prime minister of india (Current daye 2026)")
print(result)

# ui =  GradioUI(agent)
# ui.launch()
