from fastapi import APIRouter, Query

from ai.src.cleaner import HtmlSimpleCleaner

router = APIRouter(prefix="/clean")

Clean_SimpleCleaner = HtmlSimpleCleaner()


@router.post("/html/simple")
def html_simple_cleaner(html: str = Query(...)) -> str:
    return Clean_SimpleCleaner(html)
