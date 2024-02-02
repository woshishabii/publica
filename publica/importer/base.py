import re
from abc import ABC, abstractmethod


class BaseImporter(ABC):
    """
    This is the base of all the importers
    """
    identifier = 'None'
    pattern = r''

    @abstractmethod
    def __init__(self, url):
        """
        Create an importer

        btw, regex sucks
        :param url: URL of the source
        """
        self.expr = re.compile(self.pattern)
        self.url = url

    @abstractmethod
    def text(self) -> str:
        """
        This func should return the content of the url in Markdown format
        :return: Content
        """
        pass


def build_exporters() -> tuple:
    exporters = {_.identifier: _ for _ in BaseImporter.__subclasses__()}
    expressions = {_.identifier: re.compile(_.pattern) for _ in BaseImporter.__subclasses__()}
    return exporters, expressions


def get_exporter(_id: str) -> BaseImporter:
    exporters, _ = build_exporters()
    return exporters[_id]


def match_url(url: str) -> str | None:
    _, expressions = build_exporters()
    for _id, _expr in expressions.items():
        if _expr.match(url):
            return _id
    return None


def parse_url(url: str) -> str:
    exporter_id = match_url(url)
    if not exporter_id:
        raise Exception("URL Scheme not supported")
    return get_exporter(exporter_id)(url)
