from flask_restx import Resource
from . import ns
from .business import Business
from .dto import GamesDto
from flask_jwt_extended import jwt_required
from ..auth.business import token_is_revoked

@ns.doc(security=['jwt'])
@ns.route("/")
class Login(Resource):
    @ns.doc(params ={'user_id': "User's id"})
    @jwt_required()
    @token_is_revoked
    def get(self):
        return Business.get_games()

    @ns.expect(GamesDto.post_games)
    @jwt_required()
    @token_is_revoked
    def post(self):
        return Business.post_games(ns.payload)

    @ns.expect(GamesDto.put_games)
    @ns.doc(params ={'game_id': 'Game id'}, description = "Update the game by user id")
    @jwt_required()
    @token_is_revoked
    def put(self):
        return Business.put_games(ns.payload)

    @ns.doc(params ={'game_id': 'Game id'}, description = "Delete game by user id")
    @jwt_required()
    @token_is_revoked
    def delete(self):
        return Business.delete_game()
    