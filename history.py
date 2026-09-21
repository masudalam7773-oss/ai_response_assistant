def save_message(role, message):
    with open("history.txt", "a", encoding="utf-8") as file:
        file.write(f"{role}: {message}\n")


def read_history():
    try:
        with open("history.txt", "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "No conversation history found."


def clear_history():
    with open("history.txt", "w", encoding="utf-8") as file:
        file.write("")