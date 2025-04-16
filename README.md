
# LLM Business Automation Agent

This project is an **LLM-powered business automation agent** built using FastAPI and OpenAI's GPT models. It interprets natural language commands and executes relevant tools such as scheduling, summarization, and formatting — acting like a smart backend assistant.

---

## Live Demo

Access the API via Swagger UI:  
🔗 [https://llm-business-agent.onrender.com/docs](https://llm-business-agent.onrender.com/docs)

> Note: This service may take a few seconds to wake up due to Render's free tier auto-sleep.

---

## Features

- LLM-powered command interpretation
- Modular tool-calling framework
- FastAPI backend with REST endpoint
- Swagger UI for interactive testing
- Live cloud deployment via Render
- OpenAI key secured via `.env`

---

## How It Works

Send a message like:
```json
{
  "message": "Can you schedule a meeting with Alex on Friday at 3PM?"
}
```

The agent will:
- Analyze the request using GPT
- Choose a matching tool (like `schedule_meeting`)
- Generate a human-friendly response like:

```json
{
  "response": "(Used tool `schedule_meeting`)
Meeting scheduled with Alex on Friday at 3PM."
}
```

---

## API

### `POST /agent/ask`

**Request Body:**
```json
{
  "message": "Can you summarize this week's updates?"
}
```

**Response:**
```json
{
  "response": "(Used tool `summarize_text`)
Summary: ..."
}
```

---

## Run Locally

```bash
# Clone the project
git clone https://github.com/YOUR_USERNAME/llm-business-agent.git
cd llm-business-agent

# Create a virtual environment
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Add your OpenAI key to .env
echo "OPENAI_API_KEY=sk-..." > .env

# Run the app
uvicorn app.main:app --reload
```

Then open your browser to:  
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Project Structure

```
llm-business-agent/
├── app/
│   ├── agent/         # Core agent logic & tools
│   ├── api/           # API routing, controller, schemas
│   └── main.py        # FastAPI entry point
├── test/              # Local test scripts
├── .env               # OpenAI key (excluded from Git)
├── requirements.txt   # Dependencies
├── Procfile           # Render deployment config
└── README.md
```

---

## Security

`.env` is in `.gitignore`  
Your OpenAI API key is never committed  
All secrets are passed as environment variables in production

---

## Built With

- [FastAPI](https://fastapi.tiangolo.com/)
- [OpenAI API](https://platform.openai.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Render](https://render.com/)

---

## Credits

Built by Panagiotis Mavrothalassitis as part of an ML Engineering portfolio.  
Want to collaborate or see more? [lin](https://www.linkedin.com/in/pmavrothalassitis/)
