from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from backend.routes import chatbot, user

app = FastAPI()


@app.get("/")
def root():
    return RedirectResponse("/docs")


app.include_router(user.router)
app.include_router(chatbot.router)
