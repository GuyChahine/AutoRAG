from fastapi import APIRouter, Query

from ai.src.scrapper import SimpleScrapper

router = APIRouter(prefix="/scrap")

Scrap_SimpleScrapper = SimpleScrapper()


@router.post("/link/simple")
def link_simple(link: str = Query(...)) -> str:
    return Scrap_SimpleScrapper(link)
