# app/api/routes.py

from fastapi import APIRouter
from app.api.schemas import AgentRequest, AgentResponse
from app.api.controller import handle_agent_request

router = APIRouter()

@router.post("/agent/ask", response_model=AgentResponse)
def ask_agent(request: AgentRequest):
    return handle_agent_request(request)
