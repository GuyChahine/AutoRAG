from pydantic import BaseModel


class Chunk(BaseModel):
    document: str


class ChunkResponse(BaseModel):
    chunks: list[str]
