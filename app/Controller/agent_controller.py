from fastapi import APIRouter

from app.AgentLayer.request_model import (
    StartSessionRequest,
    MessageRequest,
    EndSessionRequest
)

from app.Session_Layer.session_manager import (
    create_session,
    delete_session
)

from app.AgentLayer.agent_service import process_message


router = APIRouter(prefix="/agent")

@router.post("/session/start")
def start_session(request: StartSessionRequest):

    create_session(
        request.session_id,
        request.user_id,
        request.interests,
        request.age
    )

    return {"status": "session_started"}

@router.post("/respond")
def respond(request: MessageRequest):

    response = process_message(
                request.session_id,
                request.text
                )

    return {"response": response}

@router.post("/session/end")
def end_session(request: EndSessionRequest):

    delete_session(request.session_id)

    return {"status": "session_closed"}