
from typing import Dict

sessions: Dict[str , dict] = {}

def create_session(session_id:str , user_id: str ,interest: list, age : int):

    sessions[session_id] = {
        "user_id" : user_id,
        "interests": interest,
        "age": age,
        "history":[]

    }

def get_session(session_id: str):

    return sessions.get(session_id)

def delete_session(session_id: str):

    return sessions.pop(session_id , None)

def add_to_history(session_id: str,child_text: str , agent_response: str):

    session = sessions.get(session_id)

    if not session:
        return

    session["history"].append({
        "child": child_text,
        "agent": agent_response
    })