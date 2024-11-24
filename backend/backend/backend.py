from pymongo import MongoClient
from chromadb import HttpClient

AI_URL = "http://ai:8000"

MONGO_CLIENT = MongoClient("mongo", 27017)
CHROMA_CLIENT = HttpClient("chromadb", 8000)
