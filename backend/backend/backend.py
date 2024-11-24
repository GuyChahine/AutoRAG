from pymongo import MongoClient
from chromadb import HttpClient
import os

MONGO_CLIENT = MongoClient("mongo", 27017)
CHROMA_CLIENT = HttpClient("chromadb", 8000)
