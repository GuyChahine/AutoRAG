from bs4 import BeautifulSoup


class HtmlSimpleCleaner:

    def __call__(self, html: str) -> str:
        soup = BeautifulSoup(html)
        document = soup.get_text()
        if not document:
            raise ValueError(f"No text retrieved from the html.")
        return document
