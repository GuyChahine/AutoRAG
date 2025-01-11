from fastapi import APIRouter, Body, Query, Response
from uuid import uuid4
import json

from backend.backend import CHROMA_CLIENT, AI_BASE_URL, AI_SESSION
from backend.models import chatbot as models

router = APIRouter(prefix="/chatbot")


@router.post("/create")
def add(
    user: str = Query(...),
    body: models.Add = Body(...),
) -> str:
    CHROMA_CLIENT.create_collection(
        f"{user}_{body.chatbot}", metadata={"hnsw:space": "cosine"}
    )
    return Response(status_code=200, content=f"{body.chatbot=} added for {user=}.")


@router.post("/add_document/text")
def add_document_text(
    user: str = Query(...),
    chatbot: str = Query(...),
    body: models.AddDocumentText = Body(...),
) -> str:
    res = AI_SESSION.post(AI_BASE_URL + "/clean/html/simple", json={"html": body.text})
    res = AI_SESSION.post(AI_BASE_URL + "/chunk/character", json={"document": res.text})
    documents = res.json()
    res = AI_SESSION.post(
        AI_BASE_URL + "/embed/bge_large_en_v1_5",
        json={"documents": documents},
    )
    embeded_documents = res.json()
    chromadb_collection = CHROMA_CLIENT.get_collection(f"{user}_{chatbot}")
    chromadb_collection.add(
        ids=[str(uuid4()) for _ in range(len(documents))],
        embeddings=embeded_documents,
        documents=documents,
    )
    return Response(
        status_code=200,
        content=f"text='{body.text[:50]}...', has been added to: {user=}, {chatbot=}",
    )


@router.post("/add_document/link")
def add_document_link(
    user: str = Query(...),
    chatbot: str = Query(...),
    body: models.AddDocumentLink = Body(...),
) -> str:
    res = AI_SESSION.post(AI_BASE_URL + "/scrap/link", json={"link": body.link})
    res = AI_SESSION.post(AI_BASE_URL + "/clean/html/simple", json={"html": res.text})
    res = AI_SESSION.post(AI_BASE_URL + "/chunk/character", json={"document": res.text})
    documents = res.json()
    res = AI_SESSION.post(
        AI_BASE_URL + "/embed/bge_large_en_v1_5",
        json={"documents": documents},
    )
    embeded_documents = res.json()
    chromadb_collection = CHROMA_CLIENT.get_collection(f"{user}_{chatbot}")
    chromadb_collection.add(
        ids=[str(uuid4()) for _ in range(len(documents))],
        embeddings=embeded_documents,
        documents=documents,
    )
    return Response(
        status_code=200,
        content=f"link='{body.link[:50]}...', has been added to: {user=}, {chatbot=}",
    )


@router.post("/remove_document")
def add_document_link():
    return Response(status_code=501)


@router.post("/ask")
def ask(
    user: str = Query(...),
    chatbot: str = Query(...),
    query: models.Ask = Body(...),
) -> models.AskResponse:
    res = AI_SESSION.post(
        AI_BASE_URL + "/embed/bge_large_en_v1_5",
        data=json.dumps({"documents": [query]}),
    )
    embedded_query = res.json()[0]
    chromadb_collection = CHROMA_CLIENT.get_collection(f"{user}_{chatbot}")
    query_results = chromadb_collection.query(
        query_embeddings=embedded_query, n_results=3
    )["documents"][0]
    res = AI_SESSION.post(
        AI_BASE_URL + "/llm/",
        params={
            "model": "gpt",
            "sub_model": "gpt-4o-mini",
        },
        data=json.dumps(
            {
                "query": query,
                "query_results": query_results,
            }
        ),
    )
    return models.AskResponse(output=res.json()["output"])


@router.post("/remove")
def remove(
    user: str = Query(...),
    body: models.Remove = Body(...),
) -> str:
    CHROMA_CLIENT.delete_collection(f"{user}_{body.chatbot}")
    return Response(status_code=200, content=f"{body.chatbot=} removed for {user=}.")
