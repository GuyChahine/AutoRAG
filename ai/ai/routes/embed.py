from fastapi import APIRouter, Body
from pydantic import BaseModel

from ai.src.embedding import BGELargeEnV1_5

router = APIRouter(prefix="/embed")

Embed_BGELargeEnV1_5 = BGELargeEnV1_5()


class EmbedSchema(BaseModel):
    documents: list[str]


@router.post("/bge_large_en_v1_5")
def bge_large_en_v1_5(data: EmbedSchema) -> list[list[float]]:
    return Embed_BGELargeEnV1_5(data.documents)
