# LangGraph AI Chatbot Agents

A modern, interactive AI chatbot platform built with **FastAPI** (backend) and **Streamlit** (frontend), supporting multiple LLM providers (Groq, OpenAI) and optional web search capabilities.

---

## ✨ Features

- **Multiple LLM Providers:** Seamlessly switch between Groq and OpenAI models.
- **Custom System Prompts:** Define your agent's personality and behavior.
- **Web Search Integration:** Enable real-time web search for up-to-date answers.
- **User-Friendly UI:** Clean, responsive interface powered by Streamlit.
- **FastAPI Backend:** Robust, scalable API for chat interactions.
- **Swagger UI Docs:** Instantly explore and test your API endpoints.

---

## 🚀 Quickstart

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/langgraph-chatbot.git
cd langgraph-chatbot
```

### 2. Set Up Environment Variables

Copy the example environment file and fill in your API keys:

```sh
cp .env.example .env
# Edit .env and add your GROQ, TAVILY, and OPENAI API keys
```

### 3. Install Dependencies

```sh
pip install pipenv
pipenv install
pipenv shell
```

### 4. Start the Backend

```sh
python backend.py
```

### 5. Launch the Frontend

```sh
streamlit run frontend.py
```

---

## 📖 Accessing Swagger UI Docs

Once the backend is running, open your browser and go to:

```
http://127.0.0.1:9999/docs
```

This will open the interactive **Swagger UI** for your FastAPI backend, where you can explore and test all available API endpoints.

---

## 🛠️ Project Structure

```
.
├── aiAgent.py        # Core AI agent logic and model integration
├── backend.py        # FastAPI backend server
├── frontend.py       # Streamlit frontend UI
├── .env.example      # Example environment variables
├── Pipfile           # Python dependencies
└── ...
```

---

## 🧩 Supported Models

- **Groq:** `llama-3.3-70b-versatile`, `mixtral-8x7b-32768`
- **OpenAI:** `gpt-4o-mini`

---

## 📝 Usage

1. Define your agent's system prompt in the UI.
2. Select your preferred provider and model.
3. (Optional) Enable web search for real-time information.
4. Enter your query and interact with the agent!

---

## 📄 License

MIT License

---

