# This is a sample Python script.
import os

import uvicorn
from dotenv import load_dotenv
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from fastapi import FastAPI,APIRouter
from starlette.middleware.cors import CORSMiddleware

from app.api.users import router as user_router
from app.core.config import Settings

# from app.api.v1.music.auth import router as auth_router


app = FastAPI()
router = APIRouter()
load_dotenv()  # take environment variables from .env.

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
settings = Settings()

print(settings.MONGO_URL)
print(settings.OPENAI_API_KEY)
app.include_router(user_router)





def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
