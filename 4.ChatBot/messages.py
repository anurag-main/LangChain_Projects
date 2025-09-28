from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage ,AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

messages = [
  
  SystemMessage(content="You are an software engineer"),
  HumanMessage(content="what is langchain")
]

result=model.invoke(messages)
messages.append(AIMessage(content=result.content))
print(messages)