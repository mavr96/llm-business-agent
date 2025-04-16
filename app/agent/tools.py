# app/agent/tools.py

from datetime import datetime, timedelta

def schedule_meeting(participant: str, date: str, time: str) -> str:
    """
    Simulates scheduling a meeting.
    In a real system, this would integrate with Google Calendar or Outlook.
    """
    return f"Meeting scheduled with {participant} on {date} at {time}."

def summarize_text(text: str) -> str:
    """
    Summarizes a given text. For now, a placeholder. Later, we can call an LLM.
    """
    return f"Summary: {text[:75]}..."  # Mock: return first 75 chars

def format_email_response(name: str, topic: str) -> str:
    """
    Formats a professional email response using simple template logic.
    """
    return f"""
Dear {name},

Thank you for reaching out regarding {topic}. We’ll get back to you shortly.

Best regards,  
BusinessBot
""".strip()
