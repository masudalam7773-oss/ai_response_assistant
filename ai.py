from google import genai
from config import MODEL_NAME

client = genai.Client()

chat = client.chats.create(
    model=MODEL_NAME
)
def get_ai_response(prompt):
    try:
        response = chat.send_message(prompt)
        return response.text

    except Exception as error:
      error_message = str(error)

    if "10053" in error_message or "connection" in error_message.lower():
        print("Connection Error: Please check your internet connection.")
        return "Sorry, I cannot connect to the AI right now."

    elif "429" in error_message:
        print("Gemini API quota exceeded.")
        return "Sorry, the AI API quota has been reached. Please try again later."

    elif "503" in error_message:
        print("Gemini is temporarily busy.")
        return "Sorry, Gemini is temporarily unavailable. Please try again later."

    else:
        print("AI API Error:", error)
        return "Sorry, I couldn't get a response from the AI right now."

   
def get_ai_response(prompt):
    try:
        response = chat.send_message(prompt)
        return response.text

    except Exception as error:
        error_message = str(error)

        if "10053" in error_message or "connection" in error_message.lower():
            print("Connection Error: Please check your internet connection.")
            return "Sorry, I cannot connect to the AI right now."

        elif "429" in error_message:
            print("Gemini API quota exceeded.")
            return "Sorry, the AI API quota has been reached. Please try again later."

        elif "503" in error_message:
            print("Gemini is temporarily busy.")
            return "Sorry, Gemini is temporarily unavailable. Please try again later."

        else:
            print("AI API Error:", error)
            return "Sorry, I couldn't get a response from the AI right now."

def get_python_tutor_response(prompt):
    tutor_prompt = f"""
You are a beginner-friendly Python tutor.

Teach Python in simple English.
Explain concepts step by step.
Give small examples when useful.
Do not assume the student already knows advanced programming.

Student question:
{prompt}
"""

    return get_ai_response(tutor_prompt)

def get_writing_response(prompt):
    writing_prompt = f"""
You are a helpful writing assistant.

Help the user improve or create written content.
Use clear, natural English.
Correct grammar when needed.
Keep the meaning of the user's original message.
Match the requested tone and format.
If the user asks for a rewrite, provide the finished rewritten version.

User request:
{prompt}
"""

    return get_ai_response(writing_prompt)

def get_summarizer_response(prompt):
    summarizer_prompt = f"""
You are a helpful summarization assistant.

Summarize the user's text clearly and accurately.
Keep the important information.
Remove unnecessary details.
Use simple language.
Do not add information that is not in the original text.

Text to summarize:
{prompt}
"""

    return get_ai_response(summarizer_prompt)