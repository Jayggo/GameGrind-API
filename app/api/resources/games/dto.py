from flask_restx import fields
from . import ns

class GamesDto:

    get_games = ns.model('get_games', {
        'id': fields.Integer(description = "Game id"),
        'name': fields.String(description = "Game name", required = True),
        'genre': fields.String(description = "Game genre", required = True),
        'year': fields.Integer(description = "Game year", required = True),
        'status': fields.String(description = "Game current status", required = False),
        'current_hours': fields.Integer(description = "Current played hours", required = False, default = 0),
        'active': fields.Boolean(description = "Game active status", required = False, default = True),
        'user_id': fields.Integer(description = "User id", required = True)
    })

    post_games = ns.model('post_games', {
        'name': fields.String(description = "Game name", required = True),
        'genre': fields.String(description = "Game genre", required = True),
        'year': fields.Integer(description = "Game year", required = True),
        'status': fields.String(description = "Game current status", required = False),
        'current_hours': fields.Integer(description = "Current played hours", required = False, default = 0),
        'active': fields.Boolean(description = "Game active status", required = False, default = True),
        'user_id': fields.Integer(description = "User id", required = True)
    })

    put_games = ns.model('put_games', {
        'name': fields.String(description = "Game name", required = True),
        'genre': fields.String(description = "Game genre", required = True),
        'year': fields.Integer(description = "Game year", required = True),
        'status': fields.String(description = "Game current status", required = False),
        'current_hours': fields.Integer(description = "Current played hours", required = False, default = 0),
    })