
import os
import sys
from dotenv import load_dotenv
from google.genai import types

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")

from google import genai

client = genai.Client(api_key=api_key)

user_prompt = sys.argv[1] if len(sys.argv) > 1 else None
if user_prompt == None:
    print("No prompt provided.")
    sys.exit(0)

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

response = client.models.generate_content(
                model='gemini-2.0-flash-001', 
                contents=messages
        )
print(response.text)

if "--verbose" in sys.argv:
    VERBOSE = True
    X = response.usage_metadata.prompt_token_count
    Y = response.usage_metadata.candidates_token_count
    print('User prompt:', {user_prompt})
    print('Prompt tokens:', X)
    print('Response tokens:', Y)

else:
    VERBOSE = False

if "--debug" in sys.argv:  # debugging
    DEBUG = True
    print("Argument List:", str(sys.argv))
else:
    DEBUG = False

