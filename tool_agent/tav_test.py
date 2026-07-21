from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv()
tav_api = os.environ.get("tav_key")
# print(tav_api)
client = TavilyClient(tav_api)
response = client.search("Marvel's First movie", max_results=3)
print(response)
result = response.get("results", [])
print(result)
