"""
    Created by songshiyu on 2020/10/9 上午8:35
    使用wtforms进行接收参数的验证
"""
from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange


class SearchForm(Form):
    q = StringField(validators=[DataRequired(), Length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
