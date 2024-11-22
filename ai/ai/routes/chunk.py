from fastapi import APIRouter, Query

from ai.src.chunking import CharacterChunking

router = APIRouter(prefix="/chunk")

Chunk_CharacterChunking = CharacterChunking()


@router.post("/character")
def character(document: str = Query(...)) -> list[str]:
    return Chunk_CharacterChunking(document)
