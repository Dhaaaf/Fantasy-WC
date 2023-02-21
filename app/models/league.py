from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime
# from .user import User
# from .leaguetournament import LeaguesTournament
# from .tournament import Tournament


class League(db.Model):
    __tablename__ = "leagues_table"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    display_pic = db.Column(db.String, nullable=False)
    team_budget = db.Column(db.Integer, nullable=False)
    is_private = db.Column(db.Boolean, default=False, nullable=False)

    # tournaments = db.relationship('Tournament', secondary='leagues_to_tournaments_link')
    owner = db.relationship('User', back_populates='leagues')
    user_teams = db.relationship('UserTeam', back_populates='league', cascade="all, delete-orphan")

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}
        
        tournaments = db.relationship('Tournament', secondary=f"{SCHEMA}leagues_tournaments_table")
    else:
        tournaments = db.relationship('Tournament', secondary="leagues_tournaments_table")

    def to_dict(self):
        return {
            "id": self.id,
            "owner_id": self.owner_id,
            "name": self.name,
            "display_pic": self.display_pic,
            "team_budget": self.team_budget,
            "is_private": self.is_private,
            "teams": [team.to_dict() for team in self.user_teams],
            "tournaments": [tournament.to_dict() for tournament in self.tournaments]
        }
