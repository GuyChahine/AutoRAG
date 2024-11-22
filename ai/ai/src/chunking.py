from langchain.text_splitter import CharacterTextSplitter


class CharacterChunking:

    def __init__(self):
        self.text_splitter = CharacterTextSplitter(
            separator=" ",
            chunk_size=256,
            chunk_overlap=128,
            length_function=len,
            is_separator_regex=False,
        )

    def __call__(self, document: str) -> list[str]:
        return [
            doc.page_content for doc in self.text_splitter.create_documents([document])
        ]
