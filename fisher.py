import json

from flask import Flask, make_response, jsonify
from util.helper import is_isbin_or_key

__auther__ = 'songshiyu'

from yushu_book import YuShuBook

app = Flask(__name__)

app.config.from_object('config')


@app.route('/hello/', methods={'GET'})
def hello():
    # 修改路由返回的内容
    headers = {
        'content-type': 'application/json'
        # 'location': 'www.bing.com'
    }

    response = make_response('<html></html>', 200)
    response.headers = headers
    # return "hello world"
    # return '<html></html>', 301, headers
    return response


# 搜索书籍API
@app.route('/book/search/<q>/<page>')
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


# 第二种添加路由的方式
# app.add_url_rule('/hello',view_func=hello)


if __name__ == '__main__':
    # 生产环境通常不会用Flask自带的服务器，而是使用nginx+uwsgi
    app.run(debug=app.config['DEBUG'], host='0.0.0.0', port=9999)
