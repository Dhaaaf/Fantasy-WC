from app.models import db, UserTeamPlayer, environment, SCHEMA


def seed_users_teams_players():
    utp1 = UserTeamPlayer (
        user_team_id=1,
        player_id=1
    )

    utp2 = UserTeamPlayer (
        user_team_id=1,
        player_id=16
    )

    utp3 = UserTeamPlayer (
        user_team_id=1,
        player_id=15
    )

    utp4 = UserTeamPlayer (
        user_team_id=1,
        player_id=2
    )

    utp5 = UserTeamPlayer (
        user_team_id=1,
        player_id=3
    )

    utp6 = UserTeamPlayer (
        user_team_id=1,
        player_id=5
    )

    utp7 = UserTeamPlayer (
        user_team_id=1,
        player_id=6
    )

    utp8 = UserTeamPlayer (
        user_team_id=1,
        player_id=7
    )

    utp9 = UserTeamPlayer (
        user_team_id=1,
        player_id=12
    )

    utp10 = UserTeamPlayer (
        user_team_id=1,
        player_id=13
    )

    utp11 = UserTeamPlayer (
        user_team_id=1,
        player_id=14
    )

    utp12 = UserTeamPlayer (
        user_team_id=2,
        player_id=1
    )

    utp13 = UserTeamPlayer (
        user_team_id=2,
        player_id=16
    )

    utp14 = UserTeamPlayer (
        user_team_id=2,
        player_id=15
    )

    utp15 = UserTeamPlayer (
        user_team_id=2,
        player_id=2
    )

    utp16 = UserTeamPlayer (
        user_team_id=2,
        player_id=3
    )

    utp17 = UserTeamPlayer (
        user_team_id=2,
        player_id=5
    )

    utp18 = UserTeamPlayer (
        user_team_id=2,
        player_id=6
    )

    utp19 = UserTeamPlayer (
        user_team_id=2,
        player_id=7
    )

    utp20 = UserTeamPlayer (
        user_team_id=2,
        player_id=12
    )

    utp21 = UserTeamPlayer (
        user_team_id=2,
        player_id=13
    )

    utp22 = UserTeamPlayer (
        user_team_id=2,
        player_id=14
    )

    utp23 = UserTeamPlayer (
        user_team_id=2,
        player_id=1
    )

    utp24 = UserTeamPlayer (
        user_team_id=2,
        player_id=16
    )

    utp25 = UserTeamPlayer (
        user_team_id=2,
        player_id=19
    )

    utp26 = UserTeamPlayer (
        user_team_id=2,
        player_id=2
    )

    utp27 = UserTeamPlayer (
        user_team_id=2,
        player_id=3
    )

    utp28 = UserTeamPlayer (
        user_team_id=2,
        player_id=5
    )

    utp29 = UserTeamPlayer (
        user_team_id=2,
        player_id=6
    )

    utp30 = UserTeamPlayer (
        user_team_id=2,
        player_id=7
    )

    utp31 = UserTeamPlayer (
        user_team_id=2,
        player_id=12
    )

    utp32 = UserTeamPlayer (
        user_team_id=2,
        player_id=13
    )

    utp33 = UserTeamPlayer (
        user_team_id=2,
        player_id=14
    )

    db.session.add_all(
        [
            utp1,
            utp2,
            utp3,
            utp4,
            utp5,
            utp6,
            utp7,
            utp8,
            utp9,
            utp10,
            utp11,
            utp12,
            utp13,
            utp14,
            utp15,
            utp16,
            utp17,
            utp18,
            utp19,
            utp20,
            utp21,
            utp22,
            utp23,
            utp24,
            utp25,
            utp26,
            utp27,
            utp28,
            utp29,
            utp30,
            utp31,
            utp32,
            utp33,
        ]
    )

    db.session.commit()


def undo_users_teams_players():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.user_teams_players_table RESTART IDENTITY CASCADE;"
        )
    else:
        db.session.execute("DELETE FROM user_teams_players_table")

    db.session.commit()
