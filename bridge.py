from abc import ABCMeta, abstractmethod
from typing import AnyStr, NewType
from urllib.request import Request, urlopen

Fetcher = NewType("Fetcher", "ResourceContentFetcher")


class ResourceContent:
    """interface of content"""

    def __init__(self, imp: Fetcher) -> None:
        self._imp = imp

    def show_content(self, path: AnyStr):
        """展示内容

        Args:
            - path (AnyStr): 文件路径或者网络地址
        """
        self._imp.fetch(path)


class ResourceContentFetcher(metaclass=ABCMeta):
    """Fetcher的抽象类型"""

    @abstractmethod
    def fetch(self, path: AnyStr):
        """从任何数据源获取内容

        Args:
            path (AnyStr): 文件路径或者网络地址
        """


class URLFetcher(ResourceContentFetcher):
    """从某个网址解析出内容"""

    def fetch(self, path: str):
        req = Request(path)
        with urlopen(req) as resp:
            if resp.code == 200:
                content = resp.read()
                print(content)


class LocalFileFetcher(ResourceContentFetcher):
    """从本地文件解析出内容"""

    def fetch(self, path: str):
        """从本地文件获取内容

        Args:
            - path (str): 本地文件地址
        """
        with open(path, encoding="utf-8") as fd:
            print(fd.read())
