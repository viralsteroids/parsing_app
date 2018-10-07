# -*- coding: utf-8 -*-
# ~ Author: Pavel Nikylshin
from flask import render_template, Blueprint

web = Blueprint('web', __name__, template_folder='templates')


@web.route('/')
def index():
    return render_template('index.html')


@web.route('/result')
def result():
    return render_template('result.html')
