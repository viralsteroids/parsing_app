#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Nikylshin
from flask import Blueprint
from flask_restful import Resource, reqparse, Api
from utils import parse_class

blueprint_api = Blueprint('api', __name__)
api = Api(blueprint_api)


class Service(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('text', type=str)
        args = parser.parse_args()
        text = args.get('text')
        result = None
        if text:
            _p = parse_class.NLP(text)
            result = _p.result()
        return result


api.add_resource(Service, '/service')
