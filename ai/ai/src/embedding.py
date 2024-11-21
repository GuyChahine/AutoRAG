from transformers import AutoTokenizer, AutoModel
import torch


class BGELargeEnV1_5:

    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("BAAI/bge-large-en-v1.5")
        self.model = AutoModel.from_pretrained("BAAI/bge-large-en-v1.5")
        self.model.eval()

    def __call__(self, documents: list[str]) -> list[list[float]]:
        encoded_documents = self.tokenizer(documents, return_tensors="pt")
        with torch.no_grad():
            return self.model(**encoded_documents)[0][:, 0].tolist()
