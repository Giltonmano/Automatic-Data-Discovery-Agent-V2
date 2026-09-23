import requests
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("SEMANTIC_SCHOLAR_API_KEY")
print("key loaded:", api_key)

url = "https://api.semanticscholar.org/graph/v1/paper/search"
params = {
    "query":"centrifuge",
    "fields":"title,abstract,url,year"
}
headers = {
    "x-api-key": api_key
}

response = requests.get(url, params=params)
print(response.status_code)

data = response.json()
print(data)
print(response.status_code)
print(response.headers)
print(response.text)