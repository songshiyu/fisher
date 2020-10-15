"""
    Created by songshiyu on 2020-09-28 9:45
"""

__auther__ = 'songshiyu'

from app.libs.lxkHttp import HTTP
from flask import current_app


class YuShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.total = 0
        self.books = []

    # 使用isbn搜索书籍
    def search_by_isbn(self, isbn):
        url = self.isbn_url.format(isbn)
        res = HTTP.get(url)
        self.__fill_single(res)

    # 使用keyword搜索书籍
    def search_by_keyword(self, keyword, page=1):
        url = self.keyword_url.format(keyword, current_app.config['PRE_PAGE'],
                                      self.calculate_start(page))
        res = HTTP.get(url)
        self.__fill_collection(res)

    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        self.total = data['total']
        self.books = data['books']

    def calculate_start(self, page):
        start = (page - 1) * current_app.config['PRE_PAGE']
        return start
