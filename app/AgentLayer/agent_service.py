from app.Session_Layer.session_manager import get_session, add_to_history
from app.Services.PromptBuilder.prompt_builder import build_prompt
from app.Services.LLM.LLM_service import call_LLM

def process_message(session_id:str , child_text:str) -> str:

    session = get_session(session_id)

    if not session:
        return "session not found"

    prompt = build_prompt(child_text , session)

    response = call_LLM(prompt)

    add_to_history(session_id , child_text , response)

    return response
