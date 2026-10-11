from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

class Feedback(BaseModel):

    sentiment: Literal['positive', 'negative'] = Field(description='Give the sentiment of the feedback')

# using pydantic output parser to structure our output and force to model to produce positive or negative and to ensure output format must be consistent    
parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into positive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction' : parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

# creating prompts one for each branch condition
prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

# result = classifier_chain.invoke({'feedback': 'This is a poor quality smartphone'})

# print(result)

# conditions
# branch_chain = RunnableBranch(
#     (condition1, chain1), # if
#     (condition1, chain1), # else if
#     default chain         # else
# )

positive_condition_chain = prompt2 | model | parser
negative_condition_chain = prompt3 | model | parser

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', positive_condition_chain),
    (lambda x:x.sentiment == 'negative', negative_condition_chain),
    RunnableLambda(lambda x: "could not find sentiment") 
)

chain = classifier_chain | branch_chain

result = chain.invoke({'feedback': 'This is a better quality smartphone'})

print(result)

chain.get_graph().print_ascii()