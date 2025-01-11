from fastapi import APIRouter, Body


from ai.src.scrap import Scrapper
from ai.models import scrap as models

router = APIRouter(prefix="/scrap")

Scrap_Scrapper = Scrapper()


@router.post("/link")
def link(data: models.Scrap = Body(...)) -> models.ScrapResponse:
    return Scrap_Scrapper(data.link)
