import os
from openai import OpenAI
from dotenv import load_dotenv
from llama_api_client import LlamaAPIClient

def make_llm_call(query):
    try:
        load_dotenv()
        client = OpenAI(base_url='https://api.ai-gateway.tigeranalytics.com',
                        api_key= os.getenv("OPENAI_API_KEY"))
        
        response = client.responses.create(
            model="llama-3.2-1b-instruct",
            input=query
        )
        print(response.output_text)
    except Exception:
        raise
    

def call_chatbot():
    while True:
        try:
            query = input("Ask me anything:\n").strip()
            if not query:
                continue
            make_llm_call(query)
        except (EOFError, KeyboardInterrupt):
            print("\nExiting chat.")
            break
        

if __name__=="__main__":
    call_chatbot()