import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

# Initialize Client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def ask_kortex(prompt: str) -> str:
    """Sends prompt to the latest Gemini 3 model."""
    try:
        # Using the cutting-edge model from your list
        response = client.models.generate_content(
            model="gemini-3-flash-preview", 
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"AI Engine Error: {str(e)}"

if __name__ == "__main__":
    # Connectivity test
    print(ask_kortex("System check: Is Kortex brain fully operational? Answer in one sentence."))