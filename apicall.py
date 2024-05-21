import json
import requests
import openai

headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYzVjZjdhY2MtMTQxMC00Mzk1LWEzMzgtMmE0N2FjZmY3NTAyIiwidHlwZSI6ImFwaV90b2tlbiJ9.309e55AhB4br8Fck4dlVbvqSfoax8bd6QZxG27gix0k"}

url = "https://api.edenai.run/v2/text/chat"
payload = {
    "providers": "openai",
    "text": "Hi! What do you want...",
    "chatbot_global_action": "Act as an assistant",
    "previous_history": [],
    "temperature": 0.0,
    "max_tokens": 150,
    "fallback_providers": "Deepak"
}



def take(query):
    payload["text"]=query
    #print(payload)
    response=requests.post(url,json=payload,headers=headers)
    #print(response.text)
    result=json.loads(response.text)
    print(result['openai']['generated_text'])
take("How are you...")

   
