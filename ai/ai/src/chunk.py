from langchain.text_splitter import CharacterTextSplitter

from ai.models import chunk as models


class CharacterChunking:

    def __init__(self):
        self.text_splitter = CharacterTextSplitter(
            separator=" ",
            chunk_size=256,
            chunk_overlap=128,
            length_function=len,
            is_separator_regex=False,
        )

    def __call__(self, document: str) -> models.ChunkResponse:
        chunks = [
            doc.page_content for doc in self.text_splitter.create_documents([document])
        ]
        return models.ChunkResponse(chunks=chunks)
