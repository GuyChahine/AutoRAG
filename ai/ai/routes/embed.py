from fastapi import APIRouter

from ai.src.embedding import BGELargeEnV1_5

router = APIRouter(prefix="/embed")

EMBEDDING_BGELargeEnV1_5 = BGELargeEnV1_5()


@router.post("/bge_large_en_v1_5")
def bge_large_en_v1_5(documents: list[str]):
    return {"embeddings": EMBEDDING_BGELargeEnV1_5(documents)}
