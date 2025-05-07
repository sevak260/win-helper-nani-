from ollama import chat
from ollama import ChatResponse
import requests

url = "https://api.langdock.com/openai/us/v1/chat/completions"

payload = {
    "frequency_penalty": 0,
    "logprobs": False,
    "presence_penalty": 0,
    "response_format": {"type": "text"},
    "stream": False,
    "temperature": 1,
    "top_p": 1,
    "model": "gpt-4o",
    "messages": [{
        "role": "user",
        "content": "a"
}],
}
headers = {
    "Authorization": "sk-wTCPX-sw-5L7ltDKCUE8eacImtRzxKvQ7b86YK9gv06TN8vGpZvV-_jcQVK0apzduTo4Gf0Q3ibz5SEVBfAtMw",
    "Content-Type": "application/json"
}

def create_answer_langdock(text:str) -> str:
    payload["messages"][0]["content"] = text
    response = requests.request("POST", url, json=payload, headers=headers)
    try:
        return response.json()["choices"][0]["message"]["content"]
    except:
        return 'error'

def create_answer_local(text: str) -> str:
        response: ChatResponse = chat(model='llama3.2', messages=[
            {
                'role': 'user',
                'content': text,
            },
        ])
        return response['message']['content']