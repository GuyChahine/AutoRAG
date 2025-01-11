from fastapi import APIRouter, Body


from ai.src.embed import BGELargeEnV1_5
from ai.models import embed as models

router = APIRouter(prefix="/embed")

Embed_BGELargeEnV1_5 = BGELargeEnV1_5()


@router.post("/bge_large_en_v1_5")
def bge_large_en_v1_5(body: models.Embed = Body(...)) -> models.EmbedResponse:
    return Embed_BGELargeEnV1_5(body.documents)
