from fastapi import APIRouter, Body
from pydantic import BaseModel

from ai.src.scrapper import Scrapper

router = APIRouter(prefix="/scrap")

Scrap_Scrapper = Scrapper()


class ScrapSchema(BaseModel):
    link: str


@router.post("/link")
def link(data: ScrapSchema) -> str:
    return Scrap_Scrapper(data.link)
