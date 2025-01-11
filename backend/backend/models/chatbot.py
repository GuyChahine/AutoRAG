from pydantic import BaseModel


class Add(BaseModel):
    chatbot: str


class AddDocumentText(BaseModel):
    text: str


class AddDocumentLink(BaseModel):
    link: str


class Ask(BaseModel):
    query: str


class AskResponse(BaseModel):
    output: str


class Remove(BaseModel):
    chatbot: str
