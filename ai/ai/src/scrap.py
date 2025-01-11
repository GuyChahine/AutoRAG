import requests
from fastapi import HTTPException

from ai.models import scrap as models


class Scrapper:

    def __init__(self):
        self.session = requests.Session()

    def __call__(self, link: str) -> models.ScrapResponse:
        res = self.session.get(link)
        if not res.ok:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to fetch the link '{link}'. Error: {res.text}",
            )
        if not res.content:
            raise HTTPException(
                status_code=500, detail=f"No content retrieved from the link '{link}'."
            )
        return models.ScrapResponse(html=res.text)
