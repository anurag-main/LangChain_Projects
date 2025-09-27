from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

client = InferenceClient(model="gpt2", token=token)
response = client.text_generation("Where is Pune?", max_new_tokens=50)
print(response)
