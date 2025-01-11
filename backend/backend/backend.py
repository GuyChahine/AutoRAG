from pymongo import MongoClient
from chromadb import HttpClient
import requests
from fastapi import HTTPException


def raise_for_status_hook(response, *args, **kwargs):
    if not response.ok:
        raise HTTPException(status_code=500, detail=response.text)


AI_BASE_URL = "http://ai:8000"
AI_SESSION = requests.Session()
AI_SESSION.hooks["response"].append(raise_for_status_hook)


MONGO_CLIENT = MongoClient("mongo", 27017)
CHROMA_CLIENT = HttpClient("chromadb", 8000)
