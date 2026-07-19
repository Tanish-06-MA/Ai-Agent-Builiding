from smolagents import CodeAgent, OpenAIModel
from dotenv import load_dotenv
import os

load_dotenv()

api = os.environ.get("API_KEY")

model = OpenAIModel(
    model_id="openai/gpt-oss-20b:free",
    api_base="https://openrouter.ai/api/v1",
    api_key=api,
)

agent = CodeAgent(tools=[], model=model)

result = agent.run("How to build Ai agents")
print(result)
