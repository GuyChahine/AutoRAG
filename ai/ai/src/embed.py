from transformers import AutoTokenizer, AutoModel
import torch

from ai.models import embed as models


class BGELargeEnV1_5:

    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("BAAI/bge-large-en-v1.5")
        self.model = AutoModel.from_pretrained("BAAI/bge-large-en-v1.5")
        self.model.eval()

    def __call__(self, documents: list[str]) -> models.EmbedResponse:
        tokenized_documents = self.tokenizer(
            documents, return_tensors="pt", padding=True
        )
        with torch.no_grad():
            embeded_documents = self.model(**tokenized_documents)[0][:, 0].tolist()
            return models.EmbedResponse(embeded_documents=embeded_documents)
