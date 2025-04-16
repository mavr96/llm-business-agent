# app/api/controller.py

from app.agent.agent import agent_respond
from app.api.schemas import AgentRequest, AgentResponse

def handle_agent_request(request: AgentRequest) -> AgentResponse:
    # Call your core logic (agent)
    result = agent_respond(request.message)
    return AgentResponse(response=result)
