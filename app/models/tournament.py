from .db import db, environment, SCHEMA, add_prefix_for_prod
# from .player import Player


class Tournament(db.Model):
    __tablename__ = "tournaments_table"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    tournament_name = db.Column(db.String(50), nullable=False)

    players = db.relationship('Player', back_populates='tournament', cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "tournament_name": self.tournament_name,
            # "players": [player.to_dict() for player in self.players]
        }
