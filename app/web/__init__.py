"""
    Created by songshiyu on 2020/9/29 上午9:18
"""
from flask import Blueprint

web = Blueprint('web', __name__)

from app.web import book
