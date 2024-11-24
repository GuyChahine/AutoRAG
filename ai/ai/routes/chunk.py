from fastapi import APIRouter, Body
from pydantic import BaseModel

from ai.src.chunking import CharacterChunking

router = APIRouter(prefix="/chunk")

Chunk_CharacterChunking = CharacterChunking()


class ChunkSchema(BaseModel):
    document: str


@router.post("/character")
def character(data: ChunkSchema) -> list[str]:
    return Chunk_CharacterChunking(data.document)
