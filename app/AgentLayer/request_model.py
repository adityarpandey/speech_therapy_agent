from pydantic import BaseModel
from typing import List

class StartSessionRequest(BaseModel):

    session_id: str
    user_id: str
    interests: List[str]
    age: int


class MessageRequest(BaseModel):

    session_id: str
    text: str

class EndSessionRequest(BaseModel):

    session_id:str

