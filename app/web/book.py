"""
    Created by songshiyu on 2020/9/29 上午8:25
"""

# 搜索书籍API
from flask import jsonify, request
from util.helper import is_isbin_or_key
from yushu_book import YuShuBook
from . import web
from ..forms.book import SearchForm


# @web.route('/book/search/<q>/<page>')
# def search(q, page):
# """
#:param q:普通关键字 | isbn
#:param page:
#:return:
# """
# isbin_or_key = is_isbin_or_key(q)

# if isbin_or_key == 'isbin':
#    result = YuShuBook.search_by_isbn(q)
# else:
#    result = YuShuBook.search_by_keyword(q, page)

# 原始返回json格式的数据
# return json.dumps(result), 200, {'content-type': 'application/json'}

# 使用jsonify格式化json
# return jsonify(result)


# python接受参数的另一个方式，通过？传参 request对象
# wtforms 验证层
@web.route("/book/search")
def search():
    """
        q:普通关键字
        page：页码
        ?q=金庸&page=1
    :return:
    """
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data

        isbin_or_key = is_isbin_or_key(q)

        if isbin_or_key == 'isbin':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q, page)
        return jsonify(result)
    else:
        return form
