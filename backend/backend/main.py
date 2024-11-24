from fastapi import FastAPI, Body
import requests
from uuid import uuid4
import json

from backend.backend import MONGO_CLIENT, CHROMA_CLIENT, AI_URL

app = FastAPI()


@app.get("/")
def root():
    return "backend is running!"


@app.post("/{user}/add/chatbot")
def add_chatbot(
    user: str,
    chatbot: str = Body(...),
):
    CHROMA_CLIENT.create_collection(
        f"{user}_{chatbot}", metadata={"hnsw:space": "cosine"}
    )
    return f"{chatbot=} added for {user=}."


@app.post("/{user}/update/{chatbot}/add_document/link")
def add_document_link(
    user: str,
    chatbot: str,
    link: str = Body(),
):
    res = requests.post(AI_URL + "/scrap/link", data=json.dumps({"link": link}))
    res = requests.post(
        AI_URL + "/clean/html/simple", data=json.dumps({"html": res.text})
    )
    res = requests.post(
        AI_URL + "/chunk/character", data=json.dumps({"document": res.text})
    )
    documents = res.json()
    res = requests.post(
        AI_URL + "/embed/bge_large_en_v1_5", data=json.dumps({"documents": documents})
    )
    embeded_documents = res.json()
    chromadb_collection = CHROMA_CLIENT.get_collection(f"{user}_{chatbot}")
    chromadb_collection.add(
        ids=[str(uuid4()) for _ in range(len(documents))],
        embeddings=embeded_documents,
        documents=documents,
    )
    return f"link='{link[:50]}...', has been added to: {user=}, {chatbot=}"


@app.post("/{user}/ask/{chatbot}")
def ask_chatbot(
    user: str,
    chatbot: str,
    query: str = Body(...),
):
    res = requests.post(
        AI_URL + "/embed/bge_large_en_v1_5", data=json.dumps({"documents": [query]})
    )
    embedded_query = res.json()[0]
    chromadb_collection = CHROMA_CLIENT.get_collection(f"{user}_{chatbot}")
    query_results = chromadb_collection.query(
        query_embeddings=embedded_query, n_results=3
    )
    return query_results["documents"][0]


@app.post("/{user}/remove")
def remove_chatbot(
    user: str,
    chatbot: str = Body(...),
):
    CHROMA_CLIENT.delete_collection(f"{user}_{chatbot}")
    return f"{chatbot=} removed for {user=}."
