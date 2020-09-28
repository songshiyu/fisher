"""
    Created by songshiyu on 2020-09-28 9:45
"""

__auther__ = 'songshiyu'

from util.lxkHttp import HTTP


class YuShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    # 使用isbn搜索书籍
    @staticmethod
    def search_by_isbn(isbn):
        url = YuShuBook.isbn_url.format(isbn)
        res = HTTP.get(url)
        return res

    # 使用keyword搜索书籍
    @staticmethod
    def search_by_keyword(keyword, page=1):
        url = YuShuBook.keyword_url.format(keyword, 0, 15)
        res = HTTP.get(url)
        return res