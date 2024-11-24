from fastapi import APIRouter, Body
from pydantic import BaseModel

from ai.src.cleaner import HtmlSimpleCleaner

router = APIRouter(prefix="/clean")

Clean_SimpleCleaner = HtmlSimpleCleaner()


class CleanSchema(BaseModel):
    html: str


@router.post("/html/simple")
def html_simple_cleaner(data: CleanSchema) -> str:
    return Clean_SimpleCleaner(data.html)
