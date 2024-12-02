from bs4 import BeautifulSoup
import re


class HtmlSimpleCleaner:

    def __init__(self):
        self.cleaning_regex = re.compile(r"(?:\n|[\ \\\"\'\r])+")

    def __call__(self, html: str) -> str:
        soup = BeautifulSoup(html, features="html.parser")
        document = soup.get_text(" ")
        if not document:
            raise ValueError(f"No text retrieved from the html.")
        clean_document = self.cleaning_regex.sub(" ", document).strip()
        return clean_document
