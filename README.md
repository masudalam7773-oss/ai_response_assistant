# 🤖 AI Response Assistant

A Python-based AI Response Assistant powered by the Gemini API.

This project was built to learn how to connect Python with an AI model, maintain conversations, save chat history, handle errors, and organize an AI application into separate modules.

## 🚀 Features

* 💬 AI-powered question and answer
* 🧠 Conversation context
* 💾 Conversation history
* 🐍 Python Tutor mode
* ✍️ Writing assistance mode
* 🔧 General assistant mode
* ⚠️ API and connection error handling
* 📁 Modular Python project structure
* 🔐 API key protection using environment variables

## 🏗️ Project Structure

```text
Assistant/
│
├── main.py        # Main application and chat interface
├── ai.py          # Gemini API communication
├── config.py      # Configuration
├── history.py     # Conversation history management
├── utils.py       # Utility functions
├── .gitignore     # Protects private/local files
└── README.md      # Project documentation
```

## 🔄 How It Works

```text
User
  │
  ▼
main.py
  │
  ├──► history.py
  │       │
  │       └── Conversation history
  │
  └──► ai.py
          │
          ▼
      Gemini API
          │
          ▼
       AI Response
          │
          ▼
        User
```

## 🛠️ Technologies Used

* Python
* Google Gemini API
* Google GenAI Python SDK
* Git
* GitHub

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/masudalam7773-oss/ai_response_assistant.git
```

### 2. Open the project

```bash
cd ai_response_assistant
```

### 3. Install the required package

```bash
pip install google-genai
```

### 4. Set your Gemini API key

The API key should be stored as an environment variable.

On Windows PowerShell:

```powershell
$env:GEMINI_API_KEY="YOUR_API_KEY"
```

Do not put your real API key directly into the source code or upload it to GitHub.

### 5. Run the assistant

```bash
python main.py
```

## 🎯 Project Goals

This project demonstrates practical Python skills including:

* Functions
* Modules
* File handling
* Error handling
* Environment variables
* API integration
* Conversation management
* Git and GitHub

## 📚 What I Learned

While building this project, I learned how to:

1. Connect Python to an AI API.
2. Send user prompts to an AI model.
3. Receive and display AI responses.
4. Maintain conversation context.
5. Save conversation history.
6. Handle API and connection errors.
7. Build different assistant modes.
8. Organize Python code into modules.
9. Use Git for version control.
10. Publish a Python project on GitHub.

## 🔮 Future Improvements

Possible future improvements include:

* Web-based interface
* Voice input and output
* More assistant modes
* Better conversation management
* Database-based history
* Automated testing
* Deployment as a web application

## 👨‍💻 Author

**Masud**

Python & Generative AI learner building practical AI projects.

---

⭐ If you find this project useful, feel free to explore the code and learn from it.
