from fastapi import FastAPI, Query

from backend.backend import MONGO_CLIENT, CHROMA_CLIENT

app = FastAPI()


@app.get("/")
def root():
    return "backend is running!"


@app.post("/{user}/add/chatbot")
def add_chatbot(
    user: str,
    chatbot: str = Query(...),
):
    CHROMA_CLIENT.create_collection(f"{user}_{chatbot}")
    return f"{chatbot} added."


@app.post("/{user}/update/{chatbot}/add_document/link")
def add_document_link(
    user: str,
    chatbot: str,
    link: str,
):
    # TODO
    return f"link='{link[:10]}...', has been added to: {user=}, {chatbot=}"


@app.post("/{user}/ask/{chatbot}")
def ask_chatbot():
    return ""


@app.post("/{user}/remove/{chatbot}")
def remove_chatbot():
    return ""
