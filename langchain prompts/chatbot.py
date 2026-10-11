from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

# chat_history is a list that will store the conversation history between the user and the AI model. 
# Each entry in the list will be a dictionary containing the user's input and the AI's response. 
# This allows for maintaining context in the conversation, enabling the AI to provide more relevant and coherent responses based on previous interactions.
chat_history = [
    SystemMessage(content="You are a helpful AI assistant"),
]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if(user_input.lower() == "exit"):
        break
    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print(f"AI: {response.content}")

print(chat_history)