from flask_restx import marshal
from flask import Response, request
from app.database.db import db
from app.database.models.game import Game
from .dto import GamesDto
class Business:

    @staticmethod
    def get_games():
        try:
            user_id = request.args.get('user_id')
            games = Game.query.filter_by(user_id = user_id, active = True).order_by(Game.id.asc()).all()
            if games:
                return marshal(games, GamesDto.get_games), 200
            else:
                return Response("This user hasn't have any games", 404)
        except Exception as e:
            return Response (f"ERROR: {e}", 500)
    
    @staticmethod
    def post_games(data:dict):
        try:
            name = data['name']
            genre = data['genre']
            year = data['year']
            status = data['status']
            current_hours = data['current_hours']
            active = data['active']
            user_id = data['user_id']

            new_game = Game(name, genre, year, status, current_hours, active, user_id)
            db.session.add(new_game)
            db.session.commit()

            return marshal(new_game, GamesDto.get_games), 200

        except Exception as e:
            return Response (f"ERROR: {e}", 500)

    @staticmethod
    def put_games(data:dict):
        try:
            game_id = request.args.get('game_id')

            game_found = Game.query.filter_by(id = game_id).first()

            if game_found:
                for key, value in data.items():
                    if (value is not None):
                        setattr(game_found, key, value)
                db.session.commit()

                updated_game = Game.query.filter_by(id = game_id).first()
                return marshal(updated_game, GamesDto.get_games), 200
            else:
                return Response("Game not found", 404)
        except Exception as e:
            return Response (f"ERROR: {e}", 500)

    @staticmethod
    def delete_game():
        try:
            game_id = request.args.get('game_id')
            game_found = Game.query.filter_by(id = game_id).first()

            if game_found:
                setattr(game_found, "active", 0)
                db.session.commit()
                return Response (f"{game_found.name} has been succesfully eliminated.",200)
            else:
                return Response ("Game not found", 404)

        except Exception as e:
            return Response (f"ERROR: {e}", 500)