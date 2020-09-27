from flask import Flask, make_response

__auther__ = 'songshiyu'

app = Flask(__name__)

app.config.from_object('config')


@app.route('/hello/')
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


# 搜索API
@app.route('/book/search/<q>/<page>')
def search(q, page):
    """
    :param q:普通关键字 | isbn
    :param page:
    :return:
    """
    # isbin isbin13 13个0到9的数子组成
    # isbin10 10个0到9的数数字组成，含有一些'-'
    isbin_or_key = 'key'
    if len(q) == 13 and q.isdigit:
        isbin_or_key = 'isbn'
    short_q = q.replace('-', '')
    if '-' in short_q and len(short_q) == 10 and short_q.isdigit:
        isbin_or_key = 'isbin'
    pass


# 第二种添加路由的方式
# app.add_url_rule('/hello',view_func=hello)


if __name__ == '__main__':
    # 生产环境通常不会用Flask自带的服务器，而是使用nginx+uwsgi
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=9999)
