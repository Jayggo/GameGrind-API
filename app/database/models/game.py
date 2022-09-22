from app.database.db import db
from flask import current_app
from datetime import datetime, timedelta, timezone
from app.database.models.users import Users

class Game(db.Model):

    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(100))
    genre = db.Column(db.String(100))
    year = db.Column(db.Integer())
    status = db.Column(db.String(100))
    current_hours = db.Column(db.Integer())
    active = db.Column(db.Boolean)
    user_id = db.Column(db.Integer(), db.ForeignKey(Users.id, ondelete='CASCADE', onupdate='CASCADE'), nullable = False)

    def __init__(self, name, genre, year, status, current_hours, active, user_id):
        self.name = name
        self.genre = genre
        self.year = year
        self.status = status
        self.current_hours = current_hours
        self.active = active
        self.user_id = user_id