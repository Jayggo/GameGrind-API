from flask_restx import Resource
from flask import request
from . import ns
from .business import Business
from .dto import GamesDto

@ns.route("/")
class Login(Resource):
    def get(self):
        return Business.get_games()

    @ns.expect(GamesDto.post_games)
    def post(self):
        return Business.post_games(ns.payload)