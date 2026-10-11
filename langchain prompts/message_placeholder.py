from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

# chat template
chat_template = ChatPromptTemplate(
    [
        ('system', 'You are a helpful customer support agent'),
        MessagesPlaceholder(variable_name="chat_history"),
        ('human', '{query}'),
    ]
)

# load chat history from a database or other source
chat_history = []
with open("chat_history.txt", "r") as f:
    chat_history = f.readlines()

# create a prompt with the chat history and a new query
prompt = chat_template.invoke(
    {
        "chat_history": chat_history,
        "query": HumanMessage(content="Where is my refund?"),
    }
)

print(prompt)
