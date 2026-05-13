from google import genai
import os

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def ask_gemini(prompt, system_context):

    full_prompt = f"""
{system_context}

USER REQUEST:
{prompt}
"""

    response = client.models.generate_content(
        model="gemini-2.5-pro",
        contents=full_prompt
    )

    return response.text