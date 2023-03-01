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

    ut4 = UserTeam (
        user_id=3,
        name="Experimentation",
        points=456,
        league_id=1,
        bank=15,
        match_day=7
    )

    ut5 = UserTeam (
        user_id=3,
        name="Save me Leo",
        points=463,
        league_id=2,
        bank=25,
        match_day=7
    )

    ut6 = UserTeam (
        user_id=3,
        name="Nightmare Team",
        points=414,
        league_id=3,
        bank=20,
        match_day=7
    )

    ut7 = UserTeam (
        user_id=3,
        name="Enzooooo",
        points=529,
        league_id=5,
        bank=65,
        match_day=7
    )

    ut8 = UserTeam (
        user_id=3,
        name="Di Maria's team",
        points=507,
        league_id=5,
        bank=55,
        match_day=7
    )

    ut9 = UserTeam (
        user_id=1,
        name="Football Hell",
        points=439,
        league_id=1,
        bank=15,
        match_day=7
    )

    ut10 = UserTeam (
        user_id=1,
        name="Becks",
        points=477,
        league_id=1,
        bank=23,
        match_day=7
    )

    ut11 = UserTeam (
        user_id=1,
        name="Fergie's Babes",
        points=460,
        league_id=2,
        bank=11,
        match_day=7
    )

    ut12 = UserTeam (
        user_id=1,
        name="Glazers Nooo",
        points=429,
        league_id=3,
        bank=55,
        match_day=7
    )

    ut13 = UserTeam (
        user_id=1,
        name="AGUEROOOOOOO",
        points=493,
        league_id=5,
        bank=45,
        match_day=7
    )

    ut14 = UserTeam (
        user_id=1,
        name="RVP Time",
        points=477,
        league_id=2,
        bank=12,
        match_day=7
    )

    db.session.add_all(
        [
            ut1,
            ut2,
            ut3,
            ut4,
            ut5,
            ut6,
            ut7,
            ut8,
            ut9,
            ut10,
            ut11,
            ut12,
            ut13,
            ut14
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
