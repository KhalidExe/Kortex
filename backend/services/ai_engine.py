import os
import fitz  # PyMuPDF
from google import genai
from dotenv import load_dotenv

load_dotenv()

# Initialize Gemini Client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def extract_text_from_pdf(file_path: str) -> str:
    """Extracts all text content from a PDF file."""
    try:
        text = ""
        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text()
        return text
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

def ask_kortex_with_context(context: str, query: str) -> str:
    """Sends lesson context and user query to Gemini."""
    try:
        prompt = f"""
        Context from study material:
        {context}
        
        User Question: {query}
        
        Instructions: Use the provided context to answer the question accurately. 
        If the answer is not in the context, state that clearly.
        """
        
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"AI Error: {str(e)}"

if __name__ == "__main__":
    # Minimal test
    print("AI Engine updated with PDF support.")