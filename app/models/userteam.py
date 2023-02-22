from .db import db, environment, SCHEMA, add_prefix_for_prod
# from .player import Player

class UserTeam(db.Model):
    __tablename__ = "user_teams_table"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    points = db.Column(db.Integer, nullable=False, default=0)
    league_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('leagues_table.id')), nullable=False)
    bank = db.Column(db.Integer, nullable=False)
    match_day = db.Column(db.Integer, nullable=False, default=1)

    players = db.relationship('Player', secondary='user_teams_players_table', back_populates='user_teams')

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}
        players = db.relationship('Player', secondary=f"{SCHEMA}.user_teams_players_table", back_populates="user_teams")
    else:
        players = db.relationship('Player', secondary='user_teams_players_table', back_populates='user_teams')
    
    
    user =db.relationship("User", back_populates="user_teams")
    league =db.relationship("League", back_populates="user_teams")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "name": self.name,
            "points": self.points,
            "league_id": self.league_id,
            "bank": self.bank,
            "match_day": self.match_day,
            "user": self.user.to_dict(),
            "players": [player.to_dict() for player in self.players]
        }
