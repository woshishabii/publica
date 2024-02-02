from . import BaseImporter

import wikipediaapi


class WikipediaImporter(BaseImporter):
    identifier = 'wikipedia'
    pattern = r'https?:\/\/(\w{2,3})\.wikipedia\.org\/wiki\/(\w+)'

    def __init__(self, url):
        super().__init__(url)
        self.wiki = wikipediaapi.Wikipedia("Publica", self.lang)
        self.page = self.wiki.page(self.title)

    def text(self) -> str:
        if not self.page.exists():
            raise Exception("Page Not Found")
        self.t = self.page.text.replace('\n', '\n\n\n')
        return f"""# {self.title}\n\n\n{self.t}"""

    @property
    def lang(self):
        return self.expr.findall(self.url)[0][0]

    @property
    def title(self):
        return self.expr.findall(self.url)[0][1]
