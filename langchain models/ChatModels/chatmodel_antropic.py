from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file 

# Create an instance of the Anthropic Chat model
chat_model = ChatAnthropic(model='claude-v1')

chat_model_response = chat_model.invoke("What is the capital of Pakistan?", temperature=0.7, max_completion_tokens=10)

print(chat_model_response.content)