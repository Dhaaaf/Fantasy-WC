from app.models import db, Tournament, environment, SCHEMA


def seed_tournaments():

    tournament1 = Tournament (
        tournament_name="2022 World Cup"
    )

    tournament2 = Tournament (
        tournament_name="2018 World Cup"
    )

    tournament3 = Tournament (
        tournament_name="2014 World Cup"
    )

    tournament4 = Tournament (
        tournament_name="2010 World Cup"
    )

    tournament5 = Tournament (
        tournament_name="2006 World Cup"
    )

    tournament6 = Tournament (
        tournament_name="2002 World Cup"
    )

    tournament7 = Tournament (
        tournament_name="1998 World Cup"
    )

    db.session.add_all(
        [
            tournament1,
            tournament2,
            tournament3,
            tournament4,
            tournament5,
            tournament6,
            tournament7
        ]
    )

    db.session.commit()


def undo_tournaments():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.tournaments_table RESTART IDENTITY CASCADE;"
        )
    else:
        db.session.execute("DELETE FROM tournaments_table")

    db.session.commit()
