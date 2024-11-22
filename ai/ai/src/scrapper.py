import requests
from bs4 import BeautifulSoup


class SimpleScrapper:

    def __init__(self):
        self.session = requests.Session()

    def __call__(self, link: str) -> str:
        try:
            res = self.session.get(link)
            res.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Failed to fetch the link '{link}'. Error: {e}") from e
        if not res.content:
            raise ValueError(f"No content retrieved from the link '{link}'.")

        soup = BeautifulSoup(res.text)
        document = soup.get_text()
        if not document:
            raise ValueError(f"No text retrieved from the link '{link}'.")
        return document
