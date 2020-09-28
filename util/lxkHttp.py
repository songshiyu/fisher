"""
    Created by songshiyu on 2020-09-28 9:34
    python 中调用http请求的两种方式
    ①urllib
    ②flask中的requests
"""

import requests

__auther__ = 'songshiyu'


class HTTP:

    @staticmethod
    def get(url, return_json=True):
        res = requests.get(url)

        if res.status_code != 200:
            return {} if return_json else ''
        return res.json() if return_json else res.text
