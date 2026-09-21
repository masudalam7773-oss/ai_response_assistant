from ai import get_ai_response, get_python_tutor_response, get_writing_response, get_summarizer_response
from history import save_message, read_history, clear_history
from utils import show_separator, show_mode_menu, show_mode_activation, is_valid_mode, get_mode_response

def get_ai_response(prompt):
    try:
        response = chat.send_message(prompt)
        return response.text

    except ConnectionError:
        print("Connection Error: Please check your internet connection.")
        return "Sorry, I cannot connect to the AI right now."

    except Exception as error:
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

from ai import get_ai_response, get_python_tutor_response, get_writing_response, get_summarizer_response
from history import save_message, read_history, clear_history

print("===== AI RESPONSE ASSISTANT =====")
show_separator()

show_mode_menu()

mode = input("Choose mode: ")

if is_valid_mode(mode):
    show_mode_activation(mode)

else:
    print("Invalid mode. Starting General mode.")
    mode = "1"
    show_mode_activation(mode)

while True:
    question = input("\nYou: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    if question.strip() == "":
        print("Please enter a question.")
        continue

    if question.lower() == "history":
        print("\n===== CHAT HISTORY =====")
        print(read_history())
        continue

    if question.lower() == "clear":
        clear_history()
        print("Chat history cleared!")
        continue

    save_message("User", question)

    ai_response = get_mode_response(mode, question)

    print("AI:", ai_response)

    save_message("AI", ai_response)