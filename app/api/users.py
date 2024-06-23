from fastapi import APIRouter

from app.models.chat_request import ChatRequest
from app.services.chat_service import chat_response

router = APIRouter()

@router.get("/welcome")
async def userWelcome():
    return "Hey!, Welcome to MongoDB. Please let me know how can I help you today!"

@router.post("/chat")
async def userChat(request: ChatRequest):
    print("reaching here ")
    return chat_response(request.que)
