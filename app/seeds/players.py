from app.models import db, Player, environment, SCHEMA


def seed_players():
    p1 = Player (
        first_name="Lionel",
        last_name="Messi",
        aka="Messi",
        picture="https://media.cnn.com/api/v1/images/stellar/prod/221218184732-messi-wc-trophy.jpg?c=original",
        team="Argentina",
        year="2022",
        position="Forward",
        value="15",
        tournament_id="1"
    )

    p2 = Player (
        first_name="Ronaldo",
        last_name="Nazario",
        picture="https://zalen.in/storage/news/post/s5SwkaprL8qwI1r8XYyt8BSj27a26kYHazGqw7vo.png",
        team="Brazil",
        year="2002",
        position="Forward",
        value="15",
        tournament_id="6"
    )

    db.session.add_all(
        [
            p1,
            p2
        ]
    )
    db.session.commit()


def undo_players():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.players_table RESTART IDENTITY CASCADE;"
        )
    else:
        db.session.execute("DELETE FROM players_table")

    db.session.commit()
