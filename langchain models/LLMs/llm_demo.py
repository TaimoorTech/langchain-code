from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# Create an instance of the OpenAI LLM
llm = OpenAI(model='gpt-3.5-turbo-instruct')

# Invoke the LLM with a prompt means we are asking the model a question or giving it a task to perform. In this case, we are asking it to provide the capital of Pakistan. The model will process the input and return a response based on its training and knowledge.
response = llm.invoke("What is the capital of Pakistan?")

print(response)
