# Personal AI Research & Task Assistant

A multi-agent system using LangGraph + MCP that helps collect information from the web, summarize it, extract action items, and store everything in a local knowledge base.

## ✨ Features
- 🔍 Web research using **FREE** APIs (no credit card required)
- 📝 AI-powered summarization using Google Gemini
- ✅ Automatic task extraction with deadlines
- 💾 Local knowledge base (SQLite)
- 🎨 Simple Streamlit UI
- 🤖 Multi-agent orchestration with LangGraph
......
## 🆓 100% Free Tools (No Credit Card Required)
- **Google AI Studio (Gemini)** - Free API key, no card needed
- **DuckDuckGo Search** - No API key needed
- **Wikipedia API** - No API key needed
- **Local SQLite** - Built-in Python

## 🚀 Quick Setup

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Get your FREE Google AI Studio API key:**
   - Go to https://aistudio.google.com/app/apikey
   - Click "Create API Key"
   - Copy the key (NO CREDIT CARD REQUIRED)

3. **Create `.env` file:**
```bash
GOOGLE_API_KEY=your_free_api_key_here
```

4. **Run the application:**
```bash
streamlit run app.py
```

## 📖 Usage Example
1. Enter a topic: "Learn Kubernetes in 30 days"
2. The assistant will:
   - Research using DuckDuckGo + Wikipedia (free)
   - Summarize key information with Gemini (free)
   - Generate a study plan
   - Extract actionable tasks
   - Store everything locally

## 🏗️ Architecture
- **LangGraph**: Multi-agent workflow orchestration
- **MCP Tools**: DuckDuckGo search, Wikipedia, local storage
- **Agents**: Research → Summarization → Task Extraction → Storage
- **Memory**: LangGraph state management
