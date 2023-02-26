from app.models import db, UserTeam, environment, SCHEMA

def seed_users_teams():
    ut1 = UserTeam (
        user_id=2,
        name="Bald Frauds",
        points=429,
        league_id=1,
        bank=15,
        match_day=7
    )

    ut2 = UserTeam (
        user_id=1,
        name="Hair Dryers",
        points=429,
        league_id=2,
        bank=45,
        match_day=7
    )

    ut3 = UserTeam (
        user_id=3,
        name="Dream Team",
        points=429,
        league_id=3,
        bank=25,
        match_day=7
    )

    db.session.add_all(
        [
            ut1,
            ut2,
            ut3,
        ]
    )
    db.session.commit()


def undo_users_teams():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.user_teams_table RESTART IDENTITY CASCADE;"
        )
    else:
        db.session.execute("DELETE FROM user_teams_table")

    db.session.commit()
