from langchain_huggingface import HuggingFaceEmbeddings

embedding=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

text= "Anurag is my name"

vector=embedding.embed_query(text)
print(vector)