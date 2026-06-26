from google import genai
from dotenv import load_dotenv
import os

# This will load (.env ) file.
load_dotenv()

# Read the API Key.
api_key = os.getenv("GEMINI_API_KEY")

print("API Key:", api_key)

# Client Connection.
client = genai.Client(api_key=api_key)

# Through this we can api key connected or not.
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Reply only with: Gemini Connected Successfully"
)

print(response.text)