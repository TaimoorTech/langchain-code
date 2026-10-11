# This script fetches a list of text-generation models from the Hugging Face API and prints their IDs which our access token can acccess.
import requests
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

response = requests.get(
    "https://router.huggingface.co/v1/models?pipeline_tag=text-generation",
    headers={
        "Authorization": f"Bearer {token}"
    }
)

print("Status:", response.status_code)

if response.ok:
    models = response.json().get("data", [])

    for model in models:
        print(model["id"])
else:
    print(response.text)