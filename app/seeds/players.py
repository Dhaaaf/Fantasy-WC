from app.models import db, Player, environment, SCHEMA


def seed_players():

    # ARGENTINA WC 2022
    p1 = Player (
        first_name="Lionel",
        last_name="Messi",
        aka="Messi",
        picture="https://media.cnn.com/api/v1/images/stellar/prod/221218184732-messi-wc-trophy.jpg?c=original",
        team="Argentina",
        year=2022,
        position="FW",
        value=15,
        tournament_id=1
    )

    p2 = Player (
        first_name="Emi",
        last_name="Martinez",
        aka="Martinez",
        picture="https://images2.minutemediacdn.com/image/upload/c_crop,w_4653,h_2617,x_0,y_0/c_fill,w_1440,ar_16:9,f_auto,q_auto,g_auto/images/GettyImages/mmsport/90min_en_international_web/01gmk8stj78rmh5yke9x.jpg",
        team="Argentina",
        year=2022,
        position="GK",
        value=5,
        tournament_id=1
    )

    p3 = Player (
        first_name="Marcos",
        last_name="Acuna",
        aka="Auna",
        picture="https://cdn.futbin.com/content/fifa23/img/players/p67333198.png?v=23",
        team="Argentina",
        year=2022,
        position="DF",
        value=5,
        tournament_id=1
    )

    p4 = Player (
        first_name="Lissandro",
        last_name="Martinez",
        aka="Martinez",
        picture="https://assets.goal.com/v3/assets/bltcc7a7ffd2fbf71f5/bltc9108921cb89d78c/63a6b693e3a93d5836b2a580/header.jpg",
        team="Argentina",
        year=2022,
        position="DF",
        value=5,
        tournament_id=1
    )

    p5 = Player (
        first_name="Cristian",
        last_name="Romero",
        aka="Romero",
        picture="https://i2-prod.football.london/tottenham-hotspur-fc/players/article25574953.ece/ALTERNATES/s615/0_GettyImages-1442799540.jpg",
        team="Argentina",
        year=2022,
        position="DF",
        value=5,
        tournament_id=1
    )

    p6 = Player (
        first_name="Nicolas",
        last_name="Otamendi",
        aka="Otamendi",
        picture="https://assets.goal.com/v3/assets/bltcc7a7ffd2fbf71f5/blt1fc2a5c917434207/6394522b95ed12556872bf11/ota_header.jpg?auto=webp&format=jpg&quality=100",
        team="Argentina",
        year=2022,
        position="DF",
        value=5,
        tournament_id=1
    )

    p7 = Player (
        first_name="Nahuel",
        last_name="Molina",
        aka="Molina",
        picture="https://cdn.footballfancast.com/wp-content/uploads/2022/12/nahuel-molina-argentina-chelsea-interest.jpg",
        team="Argentina",
        year=2022,
        position="DF",
        value=5,
        tournament_id=1
    )

    p8 = Player (
        first_name="Gonzalo",
        last_name="Montiel",
        aka="Montiel",
        picture="https://mscfootball.com/wp-content/uploads/2022/12/montiel-jpg-1200x675.webp",
        team="Argentina",
        year=2022,
        position="DF",
        value=5,
        tournament_id=1
    )

    p9 = Player (
        first_name="Angel",
        last_name="Di Maria",
        aka="Di Maria",
        picture="https://e00-marca.uecdn.es/assets/multimedia/imagenes/2022/12/18/16713891949677.jpg",
        team="Argentina",
        year=2022,
        position="MF",
        value=5,
        tournament_id=1
    )

    p10 = Player (
        first_name="Leandro",
        last_name="Paredes",
        aka="Paredes",
        picture="https://www.deccanherald.com/sites/dh/files/styles/article_detail/public/articleimages/2022/12/10/264257-01-02-1-1170358-1670632536.jpg?itok=ytRVgKLM",
        team="Argentina",
        year=2022,
        position="MF",
        value=5,
        tournament_id=1
    )

    p11 = Player (
        first_name="Rodrigo",
        last_name="De Paul",
        aka="De Paul",
        picture="https://images2.minutemediacdn.com/image/upload/c_crop,w_4919,h_2766,x_0,y_43/c_fill,w_1440,ar_16:9,f_auto,q_auto,g_auto/images/GettyImages/mmsport/90min_en_international_web/01gmkks70jrypvf30th3.jpg",
        team="Argentina",
        year=2022,
        position="MF",
        value=5,
        tournament_id=1
    )

    p12 = Player (
        first_name="Alexis",
        last_name="Mac Allister",
        aka="Mac Allister",
        picture="https://pbs.twimg.com/media/Fi1niMBXEBERdCt?format=jpg&name=4096x4096",
        team="Argentina",
        year=2022,
        position="MF",
        value=5,
        tournament_id=1
    )

    p13 = Player (
        first_name="Enzo",
        last_name="Fernandez",
        aka="Fernandez",
        picture="https://assets.goal.com/v3/assets/bltcc7a7ffd2fbf71f5/blt1457d546a4d5952f/639f615dddd807798bb8d7ad/Enzo_Fernandez(1).jpg?auto=webp&format=jpg&quality=100",
        team="Argentina",
        year=2022,
        position="MF",
        value=5,
        tournament_id=1
    )

    p14 = Player (
        first_name="Julian",
        last_name="Alvarez",
        aka="Alvarez",
        picture="https://i2-prod.manchestereveningnews.co.uk/incoming/article25710175.ece/ALTERNATES/s615/0_GettyImages-1245361344.jpg",
        team="Argentina",
        year=2022,
        position="FW",
        value=5,
        tournament_id=1
    )

    # Ronaldo Nazario R9 WC 2022

    p15 = Player (
        first_name="Ronaldo",
        last_name="Nazario",
        aka="Ronaldo",
        picture="https://zalen.in/storage/news/post/s5SwkaprL8qwI1r8XYyt8BSj27a26kYHazGqw7vo.png",
        team="Brazil",
        year=2002,
        position="FW",
        value=15,
        tournament_id=6
    )

    # Sneijder WC 2010

    p16 = Player (
        first_name="Wesley",
        last_name="Sneijder",
        aka="Sneijder",
        picture="https://pbs.twimg.com/media/FjtwDRgX0AcG8hq.jpg",
        team="Netherlands",
        year=2010,
        position="MF",
        value=15,
        tournament_id=4
    )

    # Germany WC 2014

    p17 = Player (

        first_name="Manuel",
        last_name="Neuer",
        aka="Neuer",
        picture="https://img.bleacherreport.net/img/images/photos/002/974/364/hi-res-fe6fde25a63a1b72b4376d79e8f5956d_crop_north.jpg?1405143592&w=3072&h=2048",
        team="Germany",
        year=2014,
        position="GK",
        value=5,
        tournament_id=3
    )

    p18 = Player (

        first_name="Benedikt",
        last_name="Höwedes",
        aka="Höwedes",
        picture="https://pbs.twimg.com/media/Djc_GcqW0AAX_2u.jpg",
        team="Germany",
        year=2014,
        position="DF",
        value=5,
        tournament_id=3
    )

    p19 = Player (
        first_name="Mats",
        last_name="Hummels",
        aka="Hummels",
        picture="https://img.bleacherreport.net/img/images/photos/002/971/482/hi-res-bce375cb21d89f6923c5976fd39f3e8c_crop_north.jpg?1404980586&w=3072&h=2048",
        team="Germany",
        year=2014,
        position="DF",
        value=5,
        tournament_id=3
    )

    p20 = Player (
        first_name="Jérôme",
        last_name="Boateng",
        aka="Boateng",
        picture="https://i.pinimg.com/originals/b2/3b/ee/b23bee7f63caee0cefc54473062fb3a8.jpg",
        team="Germany",
        year=2014,
        position="DF",
        value=5,
        tournament_id=3
    )

    p21 = Player (
        first_name="Philipp",
        last_name="Lahm",
        aka="Lahm",
        picture="https://s.ndtvimg.com/images/content/2014/jul/806/philipp-lahm-trophy-germany-fifa.jpg",
        team="Germany",
        year=2014,
        position="DF",
        value=5,
        tournament_id=3
    )

    p22 = Player (
        first_name="Sami",
        last_name="Khedira",
        aka="Khedira",
        picture="https://img.bleacherreport.net/img/images/photos/002/978/728/hi-res-67b1dba4d642c51ca766f2c70e12cc00_crop_north.jpg?1405456333&w=3072&h=2048",
        team="Germany",
        year=2014,
        position="MF",
        value=5,
        tournament_id=3
    )

    p23 = Player (
        first_name="Mesut",
        last_name="Özil",
        aka="Özil",
        picture="https://img.bleacherreport.net/img/images/photos/002/991/444/hi-res-44fe1e24ff69c65a27a5ab6e510aa2c8_crop_north.jpg?1406264055&w=3072&h=2048",
        team="Germany",
        year=2014,
        position="MF",
        value=5,
        tournament_id=3
    )

    p24 = Player (
        first_name="André",
        last_name="Schürrle",
        aka="Schürrle",
        picture="https://storage.googleapis.com/afs-prod/media/b03872ab94a94cf48ba3da7dd7049c43/2723.jpeg",
        team="Germany",
        year=2014,
        position="MF",
        value=5,
        tournament_id=3
    )

    p25 = Player (
        first_name="Mario",
        last_name="Götze",
        aka="Götze",
        picture="https://static.independent.co.uk/s3fs-public/thumbnails/image/2014/07/13/22/gotze-2.jpg?quality=75&width=982&height=726&auto=webp",
        team="Germany",
        year=2014,
        position="MF",
        value=5,
        tournament_id=3
    )

    p26 = Player (
        first_name="Toni",
        last_name="Kroos",
        aka="Kroos",
        picture="https://i.guim.co.uk/img/static/sys-images/Sport/Pix/pictures/2014/7/16/1405525594623/Germanys-midfielder-Toni--014.jpg?width=700&quality=85&auto=format&fit=max&s=2ca1c06387e4bc50680c3ce1f0c685f1",
        team="Germany",
        year=2014,
        position="MF",
        value=5,
        tournament_id=3
    )

    p27 = Player (
        first_name="Thomas",
        last_name="Müller",
        aka="Müller",
        picture="https://i.pinimg.com/736x/1f/84/18/1f8418e410f937bab44f3f20ac85c795--football-soccer-soccer-players.jpg",
        team="Germany",
        year=2014,
        position="FW",
        value=5,
        tournament_id=3
    )

    p28 = Player (
        first_name="Miroslav",
        last_name="Klose",
        aka="Klose",
        picture="https://i.ytimg.com/vi/DrAkH2dSozQ/maxresdefault.jpg",
        team="Germany",
        year=2014,
        position="FW",
        value=5,
        tournament_id=3
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
            p15,
            p16,
            p17,
            p18,
            p19,
            p20,
            p21,
            p22,
            p23,
            p24,
            p25,
            p26,
            p27,
            p28
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
