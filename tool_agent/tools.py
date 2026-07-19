from smolagents import CodeAgent, OpenAIModel, DuckDuckGoSearchTool
from dotenv import load_dotenv
import os

load_dotenv()

api =os.environ.get("API_KEY")

model=OpenAIModel(
    model_id="openai/gpt-oss-20b:free",
    api_base="https://openrouter.ai/api/v1",
    api_key=api
)

agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    model=model
)

result = agent.run("Fetch the data of all marvel movies and tell me which movie is the most famous")
print(result)