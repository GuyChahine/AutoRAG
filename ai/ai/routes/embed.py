from fastapi import APIRouter, Query

from ai.src.embedding import BGELargeEnV1_5

router = APIRouter(prefix="/embed")

Embed_BGELargeEnV1_5 = BGELargeEnV1_5()


@router.post("/bge_large_en_v1_5")
def bge_large_en_v1_5(documents: list[str] = Query(...)) -> list[list[float]]:
    return Embed_BGELargeEnV1_5(documents)
