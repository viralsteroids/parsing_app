#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Nikylshin
#sdfsdfsdfs
import os
from flask import Flask
from blueprints.web import web
from blueprints.api import blueprint_api


def configure_app(app):
    config = {
        "development": "conf.DevelopmentConfig",
        "production": "conf.ProductionConfig",
    }
    config_name = os.getenv('FLASK_ENV', 'production')
    print(config_name)
    app.config.from_object(config[config_name])


app = Flask(__name__)
configure_app(app)

# register Blueprints
app.register_blueprint(web)
app.register_blueprint(blueprint_api)
