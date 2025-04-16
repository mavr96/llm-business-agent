# test_agent_manual.py

from app.agent.agent import agent_respond

if __name__ == "__main__":
    print("------ Agent Test ------")
    user_message = "Can you schedule a meeting with Alex on Friday at 3PM?"
    response = agent_respond(user_message)
    print("User:", user_message)
    print("Agent:", response)
