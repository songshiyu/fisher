"""
    Created by songshiyu on 2020/9/29 上午8:25
"""

# 搜索书籍API
from flask import jsonify
from util.helper import is_isbin_or_key
from yushu_book import YuShuBook
from . import web


@web.route('/book/search/<q>/<page>')
def search(q, page):
    """
    :param q:普通关键字 | isbn
    :param page:
    :return:
    """
    isbin_or_key = is_isbin_or_key(q)

    if isbin_or_key == 'isbin':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q, page)

    # 原始返回json格式的数据
    # return json.dumps(result), 200, {'content-type': 'application/json'}

    # 使用jsonify格式化json
    return jsonify(result)
