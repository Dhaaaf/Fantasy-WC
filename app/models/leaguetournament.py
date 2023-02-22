from .db import db, environment, SCHEMA, add_prefix_for_prod


class LeaguesTournament(db.Model):
    __tablename__ = "leagues_tournaments_table"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}
    
    id = db.Column(db.Integer, primary_key=True)
    league_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('leagues_table.id')), nullable=False)
    tournament_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('tournaments_table.id')), nullable=False)
