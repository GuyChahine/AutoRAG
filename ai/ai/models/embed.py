from pydantic import BaseModel


class Embed(BaseModel):
    documents: list[str]


class EmbedResponse(BaseModel):
    embeded_documents: list[list[float]]
