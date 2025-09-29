from langchain_openai import ChatOpenAI 
from dotenv import load_dotenv
from typing import TypedDict ,Annotated ,Literal
load_dotenv()

model = ChatOpenAI()

class Review(TypedDict):
  summary : Annotated[str,'write a review Summury in 10 words']
  sentiment : Annotated[Literal['reaction+', 'reaction-'], 'Write a sentiment as positve or negative']
  

structured_model = model.with_structured_output(Review)


result = structured_model.invoke("The hardware is great but softwaere feels bloated . There are many preinstalled apps that i can not remove .also the UI looks outdated ")

print(result['sentiment'])
