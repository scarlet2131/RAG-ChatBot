from pydantic import BaseModel


class ChatRequest(BaseModel):
    que: str
