from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.output_parsers import StructuredOutputParser ,ResponseSchema
from langchain_core.prompts import PromptTemplate


load_dotenv()

model = ChatOpenAI()

schema =[
  ResponseSchema (name ='fact 1',description='fact 1 about the topic'),
  ResponseSchema (name ='fact 2',description='fact 2 about the topic'),
  ResponseSchema (name ='fact 3',description='fact 3 about the topic'),
]

parser =StructuredOutputParser.from_response_schemas(schema)

template =PromptTemplate(
  template='Give 3 facts about {topic} \n {format_instructions}',
  input_variables=['topic'],
  partial_variables={'format_instructions': parser.get_format_instructions()}
)

chain= template | model | parser

result =chain.invoke({'topic':'black rock'})
print(result)



