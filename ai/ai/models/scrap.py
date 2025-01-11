from pydantic import BaseModel


class Scrap(BaseModel):
    link: str


class ScrapResponse(BaseModel):
    html: str
