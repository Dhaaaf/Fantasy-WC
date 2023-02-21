from .db import db, environment, SCHEMA, add_prefix_for_prod


class GameWeekStat(db.Model):
    _tablename__ = "game_week_stats_table"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    week = db.Column(db.Integer, nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('players_table.id'), nullable=False)
    points = db.Column(db.Integer, nullable=False)
    goals = db.Column(db.Integer, nullable=False)
    assists = db.Column(db.Integer, nullable=False)
    clean_sheet = db.Column(db.Boolean, nullable=False)
    man_of_the_match = db.Column(db.Boolean, nullable=False)

    player = db.relationship('Player', back_populates='game_week_stats')

    def to_dict(self):
        return {
            "id": self.id,
            "week": self.week,
            "player_id": self.player_id,
            "points": self.points,
            "goals": self.goals,
            "assists": self.assists,
            "clean_sheet": self.clean_sheet,
            "man_of_the_match": self.man_of_the_match
        }
