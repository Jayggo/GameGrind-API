from flask_restx import marshal
from flask import Flask, Response, jsonify
from app.database.db import db
from app.database.models.game import Game
from .dto import GamesDto
class Business:

    @staticmethod
    def get_games():
        try:
            games = Game.query.order_by(Game.id.asc()).all()
            if games is not None:
                return marshal(games, GamesDto.get_games), 200
            else:
                return Response("Not found", 404)
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