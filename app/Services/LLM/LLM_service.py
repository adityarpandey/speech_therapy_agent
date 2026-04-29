import google.generativeai as genai
import os
from dotenv import load_dotenv
# import requests

load_dotenv()

genai.configure(api_key=os.getenv("LLM_KEY"))

# print("\nAvailable Models:\n")
#
# try:
#     models = genai.list_models()
#     for m in models:
#         print(m.name)
# except Exception as e:
#     print("Error fetching models:", e)

model = genai.GenerativeModel("gemini-2.5-flash")

print("API KEY:", os.getenv("LLM_KEY"))


def call_LLM(prompt: str) -> str:

    try:
        response = model.generate_content(prompt)

        return response.text if response.text else "Let's try again!"

    except Exception as e:
        print("Gemini Error:", e)
        return "I'm having trouble responding right now."

    # headers = {
    #     "Authorization":f"bearer{LLM_API_KEY}",
    #     "Content-Type": "application/json"
    # }
    #
    #
    # payload = {
    #     "model":MODEL_NAME,
    #     "message":[
    #         {
    #             "role":"system",
    #             "content":prompt
    #         }
    #     ],
    #
    #     "temperature":0.4
    # }
    #
    # try:
    #     response = requests.post(
    #         LLM_URL,
    #         headers=headers,
    #         json=payload,
    #         timeout=30
    #     )
    #
    #     response.raise_for_status()
    #
    #     data = response.json()
    #
    #     return data["choices"][0]["message"]["content"]
    # except requests.exceptions.RequestException as e:
    #     print("LLM_API_ERROR:" , e)
    #     return "I'm sorry, I couldn't respond right now."

# def call_LLM(prompt: str) -> str:
#     """
#     Mock LLM response for testing
#     """
#
#     print("Prompt sent to LLM:")
#     print(prompt)
#
#     # Fake response logic
#     if "rabbit" in prompt.lower():
#         return "Great job! You said rabbit correctly."
#
#     if "wabbit" in prompt.lower():
#         return "Nice try! Let's say rabbit slowly."
#
#     return "Let's practice saying some fun words together!"

# OLLAMA_URL = "http://localhost:11434/api/generate"
# MODEL_NAME = "llama3.1:8b"   # change if needed (mistral, gemma, etc.)
#
# def call_LLM(prompt: str) -> str:
#     try:
#         response = requests.post(
#             OLLAMA_URL,
#             json={
#                 "model": MODEL_NAME,
#                 "prompt": prompt,
#                 "stream": False
#             },
#             timeout=60
#         )
#
#         response.raise_for_status()
#         data = response.json()
#
#         return data.get("response", "").strip() or "Let's try again!"
#
#     except Exception as e:
#         print("LLM Error:", e)
#         return "I'm having trouble responding right now."
