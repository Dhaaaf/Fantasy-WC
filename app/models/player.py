from .db import db, environment, SCHEMA, add_prefix_for_prod
# from .gameweekstat import GameWeekStats


class Player(db.Model):
    __tablename__ = "players_table"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    aka = db.Column(db.String(50), nullable=False)
    picture = db.Column(db.String, nullable=False)
    team = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    position = db.Column(db.String(20), nullable=False)
    value = db.Column(db.Integer, nullable=False)

    tournament_id = db.Column(db.Integer, db.ForeignKey('tournaments_table.id'), nullable=False)

    game_week_stats = db.relationship('GameWeekStat', back_populates='player', cascade="all, delete-orphan")
    tournament = db.relationship('Tournament', back_populates='players')


    # user_teams = db.relationship('UserTeam', secondary='user_teams_to_player_link', back_populates="players")

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}
        user_teams = db.relationship('UserTeam', secondary=f"{SCHEMA}user_teams_players_table", back_populates="players")
    else:
        user_teams = db.relationship('UserTeam', secondary='user_teams_players_table', back_populates="players")

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "aka": self.aka,
            "picture": self.picture,
            "team": self.team,
            "year": self.year,
            "position": self.position,
            "value": self.value,
            "tournament_id": self.tournament_id,
            "stats": [stats.to_dict() for stats in self.game_week_stats]
        }
