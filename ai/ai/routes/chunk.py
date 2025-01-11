from fastapi import APIRouter, Body

from ai.src.chunk import CharacterChunking
from ai.models import chunk as models

router = APIRouter(prefix="/chunk")

Chunk_CharacterChunking = CharacterChunking()


@router.post("/character")
def character(body: models.Chunk = Body(...)) -> models.ChunkResponse:
    return Chunk_CharacterChunking(body.document)
