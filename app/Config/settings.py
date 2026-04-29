
import os
from dotenv import load_dotenv

load_dotenv()

LLM_API_KEY = os.getenv("LLM_API_KEY")
MODEL_NAME = "gemini-1.5-flash"
LLM_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=AIzaSyArh5A0c5LwWp8FnHbn-kfansztMZ9peMI"