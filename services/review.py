import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Initialize the ChatGoogleGenerativeAI instance
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    max_tokens=1500,  # Increased max_tokens for more detailed responses
    timeout=None,
    max_retries=2,
)

def review_code(code, language):
    try:
        # Get the API key from environment variables
        google_api_key = os.getenv("GOOGLE_API_KEY")

        if google_api_key:
            os.environ["GOOGLE_API_KEY"] = google_api_key
        else:
            raise ValueError("Google API Key not found in environment variables.")

        # Define the messages to invoke the AI
        messages = [
            {
                "role": "system",
                "content": f"You are a code review assistant that reviews {language} code. Provide feedback on the following code:"
                           "and provide feedback including line-by-line comments, detected "
                           "issues with severity levels (Low, Medium, High), and overall "
                           "suggestions for improvement.",
            },
            {
                "role": "human",
                "content": f"code: ```{code}```",
            },
        ]

        # Invoke the AI and get the response
        response = llm.invoke(messages)

        # Extract response content
        ai_msg = response.content.strip()  # Get the generated text

        return ai_msg

    except Exception as e:
        return f"Error: {e}"
