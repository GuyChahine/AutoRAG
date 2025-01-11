from fastapi import APIRouter, Body


from ai.src.clean import HtmlSimpleCleaner
from ai.models import clean as models

router = APIRouter(prefix="/clean")

Clean_SimpleCleaner = HtmlSimpleCleaner()


@router.post("/html/simple")
def html_simple_cleaner(body: models.Clean = Body(...)) -> models.CleanResponse:
    return Clean_SimpleCleaner(html=body.document)
