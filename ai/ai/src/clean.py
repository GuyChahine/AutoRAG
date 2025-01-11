from bs4 import BeautifulSoup
import re
from fastapi import HTTPException

from ai.models import clean as models


class HtmlSimpleCleaner:

    def __init__(self):
        self.cleaning_regex = re.compile(r"(?:\n|[\ \\\"\'\r])+")

    def __call__(self, html: str) -> models.CleanResponse:
        soup = BeautifulSoup(html, features="html.parser")
        document = soup.get_text(" ")
        if not document:
            raise HTTPException(
                status_code=500, detail=f"No text retrieved from the html."
            )
        clean_document = self.cleaning_regex.sub(" ", document).strip()
        return models.CleanResponse(clean_document=clean_document)
