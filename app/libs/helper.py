"""
 Created by songshiyu on 2020-09-28 9:12
"""

# 工具类
__auther__ = 'songshiyu'


def is_isbin_or_key(word):
    # isbin isbin13 13个0到9的数子组成
    # isbin10 10个0到9的数数字组成，含有一些'-'
    isbin_or_key = 'key'
    if len(word) == 13 and word.isdigit:
        isbin_or_key = 'isbin'
    short_word = word.replace('-', '')
    if '-' in short_word and len(short_word) == 10 and short_word.isdigit:
        isbin_or_key = 'isbin'
    return isbin_or_key
