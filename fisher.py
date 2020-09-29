from flask import make_response
from app import create_app

__auther__ = 'songshiyu'

app = create_app()


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


# 第二种添加路由的方式
# app.add_url_rule('/hello',view_func=hello)


if __name__ == '__main__':
    # 生产环境通常不会用Flask自带的服务器，而是使用nginx+uwsgi
    app.run(debug=app.config['DEBUG'], host='0.0.0.0', port=9999)
