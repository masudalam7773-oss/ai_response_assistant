def show_separator():
    print("-" * 50)


def show_mode_menu():
    print("Choose your mode:")
    print("1. General")
    print("2. Python Tutor")
    print("3. Writing")
    print("4. Summarizer")
    print("Type 'exit' to quit.")


def show_mode_activation(mode):
    if mode == "1":
        print("General mode activated.")

    elif mode == "2":
        print("Python Tutor mode activated.")

    elif mode == "3":
        print("Writing mode activated.")

    elif mode == "4":
        print("Summarizer mode activated.")

def is_valid_mode(mode):
    return mode in ["1", "2", "3", "4"]

def get_mode_response(mode, question):
    if mode == "2":
        from ai import get_python_tutor_response
        return get_python_tutor_response(question)

    elif mode == "3":
        from ai import get_writing_response
        return get_writing_response(question)

    elif mode == "4":
        from ai import get_summarizer_response
        return get_summarizer_response(question)

    else:
        from ai import get_ai_response
        return get_ai_response(question)