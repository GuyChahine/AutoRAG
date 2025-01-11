from pydantic import BaseModel


class Clean(BaseModel):
    document: str

class CleanResponse(BaseModel):
    clean_document: str