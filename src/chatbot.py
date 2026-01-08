import os

from openai import OpenAI
from dotenv import load_dotenv
from llama_api_client import LlamaAPIClient

from utils.file import load_configs

def make_llm_call(query):
    try:
        load_dotenv()
        settings = load_configs('config/llm_settings.yaml')

        client = OpenAI(base_url='https://api.ai-gateway.tigeranalytics.com',
                        api_key= os.getenv("OPENAI_API_KEY"))
        
        response = client.chat.completions.create(
            messages = [
                {"role": "system", "content": "You are a helpful assistant that provides concise answers."},
                {"role": "user", "content": f"{query}"}
            ],
            stream = True,
            **settings
        )
        # print(response.choices[0].message.content)
        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                print(chunk.choices[0].delta.content, end="")
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