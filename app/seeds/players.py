from app.models import db, Player, environment, SCHEMA


def seed_players():

    # ARGENTINA WC 2022
    p1 = Player (
        first_name="Lionel",
        last_name="Messi",
        aka="Messi",
        picture="https://media.cnn.com/api/v1/images/stellar/prod/221218184732-messi-wc-trophy.jpg?c=original",
        team="Argentina",
        year="2022",
        position="FW",
        value="15",
        tournament_id="1"
    )

    p2 = Player (
        first_name="Emi",
        last_name="Martinez",
        aka="Martinez",
        picture="https://images2.minutemediacdn.com/image/upload/c_crop,w_4653,h_2617,x_0,y_0/c_fill,w_1440,ar_16:9,f_auto,q_auto,g_auto/images/GettyImages/mmsport/90min_en_international_web/01gmk8stj78rmh5yke9x.jpg",
        team="Argentina",
        year="2022",
        position="GK",
        value="6",
        tournament_id="1"
    )

    p3 = Player (
        first_name="Marcos",
        last_name="Acuna",
        aka="Auna",
        picture="https://cdn.futbin.com/content/fifa23/img/players/p67333198.png?v=23",
        team="Argentina",
        year="2022",
        position="DF",
        value="6",
        tournament_id="1"
    )

    p4 = Player (
        first_name="Lissandro",
        last_name="Martinez",
        aka="Martinez",
        picture="https://assets.goal.com/v3/assets/bltcc7a7ffd2fbf71f5/bltc9108921cb89d78c/63a6b693e3a93d5836b2a580/header.jpg",
        team="Argentina",
        year="2022",
        position="DF",
        value="6",
        tournament_id="1"
    )

    p5 = Player (
        first_name="Cristian",
        last_name="Romero",
        aka="Romero",
        picture="https://i2-prod.football.london/tottenham-hotspur-fc/players/article25574953.ece/ALTERNATES/s615/0_GettyImages-1442799540.jpg",
        team="Argentina",
        year="2022",
        position="DF",
        value="6",
        tournament_id="1"
    )

    p6 = Player (
        first_name="Nicolas",
        last_name="Otamendi",
        aka="Otamendi",
        picture="https://assets.goal.com/v3/assets/bltcc7a7ffd2fbf71f5/blt1fc2a5c917434207/6394522b95ed12556872bf11/ota_header.jpg?auto=webp&format=jpg&quality=100",
        team="Argentina",
        year="2022",
        position="DF",
        value="6",
        tournament_id="1"
    )

    p7 = Player (
        first_name="Nahuel",
        last_name="Molina",
        aka="Molina",
        picture="https://cdn.footballfancast.com/wp-content/uploads/2022/12/nahuel-molina-argentina-chelsea-interest.jpg",
        team="Argentina",
        year="2022",
        position="DF",
        value="6",
        tournament_id="1"
    )

    p8 = Player (
        first_name="Gonzalo",
        last_name="Montiel",
        aka="Montiel",
        picture="https://mscfootball.com/wp-content/uploads/2022/12/montiel-jpg-1200x675.webp",
        team="Argentina",
        year="2022",
        position="DF",
        value="6",
        tournament_id="1"
    )

    p9 = Player (
        first_name="Angel",
        last_name="Di Maria",
        aka="Di Maria",
        picture="https://e00-marca.uecdn.es/assets/multimedia/imagenes/2022/12/18/16713891949677.jpg",
        team="Argentina",
        year="2022",
        position="MF",
        value="7",
        tournament_id="1"
    )

    p10 = Player (
        first_name="Leandro",
        last_name="Paredes",
        aka="Paredes",
        picture="https://www.deccanherald.com/sites/dh/files/styles/article_detail/public/articleimages/2022/12/10/264257-01-02-1-1170358-1670632536.jpg?itok=ytRVgKLM",
        team="Argentina",
        year="2022",
        position="MF",
        value="6",
        tournament_id="1"
    )

    p11 = Player (
        first_name="Rodrigo",
        last_name="De Paul",
        aka="De Paul",
        picture="https://images2.minutemediacdn.com/image/upload/c_crop,w_4919,h_2766,x_0,y_43/c_fill,w_1440,ar_16:9,f_auto,q_auto,g_auto/images/GettyImages/mmsport/90min_en_international_web/01gmkks70jrypvf30th3.jpg",
        team="Argentina",
        year="2022",
        position="MF",
        value="6",
        tournament_id="1"
    )

    p12 = Player (
        first_name="Alexis",
        last_name="Mac Allister",
        aka="Mac Allister",
        picture="https://pbs.twimg.com/media/Fi1niMBXEBERdCt?format=jpg&name=4096x4096",
        team="Argentina",
        year="2022",
        position="MF",
        value="7",
        tournament_id="1"
    )

    p13 = Player (
        first_name="Enzo",
        last_name="Fernandez",
        aka="Fernandez",
        picture="https://assets.goal.com/v3/assets/bltcc7a7ffd2fbf71f5/blt1457d546a4d5952f/639f615dddd807798bb8d7ad/Enzo_Fernandez(1).jpg?auto=webp&format=jpg&quality=100",
        team="Argentina",
        year="2022",
        position="MF",
        value="7",
        tournament_id="1"
    )

    p14 = Player (
        first_name="Julian",
        last_name="Alvarez",
        aka="Alvarez",
        picture="https://i2-prod.manchestereveningnews.co.uk/incoming/article25710175.ece/ALTERNATES/s615/0_GettyImages-1245361344.jpg",
        team="Argentina",
        year="2022",
        position="FW",
        value="6",
        tournament_id="1"
    )

    # BRAZIL WC 2022

    p15 = Player (
        first_name="Ronaldo",
        last_name="Nazario",
        picture="https://zalen.in/storage/news/post/s5SwkaprL8qwI1r8XYyt8BSj27a26kYHazGqw7vo.png",
        team="Brazil",
        year="2002",
        position="FW",
        value="15",
        tournament_id="6"
    )

    db.session.add_all(
        [
            p1,
            p2,
            p3,
            p4,
            p5,
            p6,
            p7,
            p8,
            p9,
            p10,
            p11,
            p12,
            p13,
            p14,
            # p15,
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
