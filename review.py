import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def review_code(code: str, language: str = "python") -> str:
    """
    Sends the provided code to the LLM and returns a structured review.
    """

    prompt = f"""
You are an expert code reviewer.

Review the following {language} code. Provide:
1. Summary of what the code does
2. Major issues
3. Minor issues
4. Security concerns
5. Suggestions for improvement
6. Optimized version if needed

Code:
