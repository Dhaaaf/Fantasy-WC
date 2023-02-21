from app.models import db, LeaguesTournament, environment, SCHEMA


def seed_leagues_tournaments():

    lt1 = LeaguesTournament (
        league_id="1",
        tournament_id="1"
    )

    lt2 = LeaguesTournament (
        league_id="1",
        tournament_id="2"
    )

    lt3 = LeaguesTournament (
        league_id="1",
        tournament_id="3"
    )

    lt4 = LeaguesTournament (
        league_id="1",
        tournament_id="4"
    )

    lt5 = LeaguesTournament (
        league_id="1",
        tournament_id="5"
    )

    lt6 = LeaguesTournament (
        league_id="1",
        tournament_id="6"
    )

    lt7 = LeaguesTournament (
        league_id="1",
        tournament_id="7"
    )

    lt8 = LeaguesTournament (
        league_id="2",
        tournament_id="7"
    )

    lt9 = LeaguesTournament (
        league_id="2",
        tournament_id="6"
    )

    lt10 = LeaguesTournament (
        league_id="2",
        tournament_id="5"
    )

    lt11 = LeaguesTournament (
        league_id="2",
        tournament_id="4"
    )

    lt12 = LeaguesTournament (
        league_id="3",
        tournament_id="4"
    )

    lt13 = LeaguesTournament (
        league_id="3",
        tournament_id="3"
    )

    lt14 = LeaguesTournament (
        league_id="3",
        tournament_id="2"
    )

    lt15 = LeaguesTournament (
        league_id="3",
        tournament_id="2"
    )

    lt16 = LeaguesTournament (
        league_id="2",
        tournament_id="1"
    )

    lt17 = LeaguesTournament (
        league_id="4",
        tournament_id="1"
    )

    lt18 = LeaguesTournament (
        league_id="5",
        tournament_id="1"
    )

    db.session.add_all(
        [
            lt1,
            lt2,
            lt3,
            lt4,
            lt5,
            lt6,
            lt7,
            lt8,
            lt9,
            lt10,
            lt11,
            lt12,
            lt13,
            lt14,
            lt15,
            lt16,
            lt17,
            lt18
        ]
    )

    db.session.commit()


def undo_leagues_tournaments():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.leagues_tournaments_table RESTART IDENTITY CASCADE;"
        )
    else:
        db.session.execute("DELETE FROM leagues_tournaments_table")

    db.session.commit()
