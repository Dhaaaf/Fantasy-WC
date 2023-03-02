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
        aka="Acuna",
        picture="https://i0.wp.com/cdn.footballfancast.com/wp-content/uploads/2022/11/Reported-Wolves-target-Marcos-Acuna-scaled-e1669821567707.jpg",
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
        picture="https://imgsrv2.voi.id/w6pLz7BZHP1p4TmzOAOl8a4uIqVVCL8j9jfxv6N8Ymc/auto/1200/675/sm/1/bG9jYWw6Ly8vcHVibGlzaGVycy8yMjQxNjcvMjAyMjExMDMwNjIwLW1haW4ucG5n.jpg",
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
        value=13,
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

    # SPAIN WC 2010

    p29 = Player (
        first_name="Iker",
        last_name="Casillas",
        aka="Casillas",
        picture="https://i.dailymail.co.uk/1s/2020/08/04/12/31547300-8591685-image-a-9_1596540025615.jpg",
        team="Spain",
        year=2010,
        position="GK",
        value=5,
        tournament_id=4
    )

    p30 = Player (
        first_name="Gerard",
        last_name="Piqué",
        aka="Piqué",
        picture="https://pbs.twimg.com/media/E6BFGgJWQAU2mOV?format=jpg&name=4096x4096",
        team="Spain",
        year=2010,
        position="DF",
        value=5,
        tournament_id=4
    )

    p31 = Player (
        first_name="Sergio",
        last_name="Ramos",
        aka="Ramos",
        picture="https://e00-marca.uecdn.es/assets/multimedia/imagenes/2020/07/10/15943994776546.jpg",
        team="Spain",
        year=2010,
        position="DF",
        value=5,
        tournament_id=4
    )
    
    p32 = Player (
        first_name="Carles",
        last_name="Puyol",
        aka="Puyol",
        picture="https://ichef.bbci.co.uk/news/976/cpsprodpb/5A4D/production/_90471132_gettyimages-107064379.jpg",
        team="Spain",
        year=2010,
        position="DF",
        value=5,
        tournament_id=4
    )

    p33 = Player (
        first_name="Sergio",
        last_name="Busquets",
        aka="Busquets",
        picture="https://pbs.twimg.com/media/CnfRmooW8AAsVpj.jpg",
        team="Spain",
        year=2010,
        position="MF",
        value=5,
        tournament_id=4
    )

    p34 = Player (
        first_name="Xabi",
        last_name="Alonso",
        aka="Alonso",
        picture="https://www.ihavenet.com/images/2010-FIFA-World-Cup-Final-Champions-Spain-Midfielder-Alonso-Xavi-with-FIFA-World-Cup-Trophy.jpg",
        team="Spain",
        year=2010,
        position="MF",
        value=5,
        tournament_id=4
    )

    p35 = Player (
        first_name="Cesc",
        last_name="Fàbregas",
        aka="Fàbregas",
        picture="https://media.cnn.com/api/v1/images/stellar/prod/200729163551-03-cesc-fabregas.jpg?q=w_2000,h_1494,x_0,y_0,c_fill",
        team="Spain",
        year=2010,
        position="MF",
        value=5,
        tournament_id=4
    )

    p36 = Player (
        first_name="Xavi",
        last_name="Hernandez",
        aka="Xavi",
        picture="https://static0.givemesportimages.com/wordpress/wp-content/uploads/2022/01/21_11_06_3dba81957cc31cb6156497cac627327a_960-1.jpg",
        team="Spain",
        year=2010,
        position="MF",
        value=5,
        tournament_id=4
    )

    p37 = Player (
        first_name="Andres",
        last_name="Iniesta",
        aka="Iniesta",
        picture="https://e0.365dm.com/15/06/2048x1152/andres-iniesta-spain-netherlands-2010-world-cup-final_3313094.jpg",
        team="Spain",
        year=2010,
        position="MF",
        value=5,
        tournament_id=4
    )

    p38 = Player (
        first_name="David",
        last_name="Villa",
        aka="Villa",
        picture="https://c3.thejournal.ie/media/2018/12/soccer-2010-fifa-world-cup-south-africa-group-h-spain-v-honduras-ellis-park-752x501.jpg",
        team="Spain",
        year=2010,
        position="FW",
        value=5,
        tournament_id=4
    )

    # FRANCE WC 2018

    p39 = Player (
        first_name="Hugo",
        last_name="Lloris",
        aka="Lloris",
        picture="https://pbs.twimg.com/media/DujzDKmW4AAR6DP.jpg",
        team="France",
        year=2018,
        position="GK",
        value=5,
        tournament_id=2
    )

    p40 = Player (
        first_name="Lucas",
        last_name="Hernandez",
        aka="L. Hernandez",
        picture="https://dynaimage.cdn.cnn.com/cnn/c_fill,g_auto,w_1200,h_675,ar_16:9/https%3A%2F%2Fcdn.cnn.com%2Fcnnnext%2Fdam%2Fassets%2F190327215215-lucas-hernandez-tease.jpg",
        team="France",
        year=2018,
        position="DF",
        value=5,
        tournament_id=2
    )

    p41 = Player (
        first_name="Benjamin",
        last_name="Pavard",
        aka="Pavard",
        picture="https://static01.nyt.com/images/2018/07/03/sports/00pavard1/merlin_140582979_12494f65-cf04-48b8-bfb8-b1062e46f050-superJumbo.jpg",
        team="France",
        year=2018,
        position="DF",
        value=5,
        tournament_id=2
    )

    p42 = Player (
        first_name="Samuel",
        last_name="Umtiti",
        aka="Umtiti",
        picture="https://cdn.vox-cdn.com/thumbor/ro2NG7bQIdFzvEjZwYUg0PjvAe0=/0x0:3000x2041/1200x800/filters:focal(1323x357:1803x837)/cdn.vox-cdn.com/uploads/chorus_image/image/60383939/999475836.jpg.0.jpg",
        team="France",
        year=2018,
        position="DF",
        value=5,
        tournament_id=2
    )

    p43 = Player (
        first_name="Raphaël",
        last_name="Varane",
        aka="Varane",
        picture="https://www.realmadrid.com/cs/Satellite?blobcol=urldata&blobheader=image%2Fjpeg&blobkey=id&blobtable=MungoBlobs&blobwhere=1203395997683&ssbinary=true",
        team="France",
        year=2018,
        position="DF",
        value=5,
        tournament_id=2
    )

    p44 = Player (
        first_name="Blaise",
        last_name="Matuidi",
        aka="Matuidi",
        picture="https://www.juventus.com/images/image/private/t_editorial_landscape_12_desktop/dev/foc6gdv1mbezkzressfn.jpg",
        team="France",
        year=2018,
        position="MF",
        value=5,
        tournament_id=2
    )

    p45 = Player (
        first_name="N'Golo",
        last_name="Kanté",
        aka="Kanté",
        picture="https://www.thesun.co.uk/wp-content/uploads/2018/07/NINTCHDBPICT000420698090.jpg?strip=all&w=960",
        team="France",
        year=2018,
        position="MF",
        value=5,
        tournament_id=2
    )

    p46 = Player (
        first_name="Paul",
        last_name="Pogba",
        aka="Pogba",
        picture="https://www.si.com/.image/t_share/MTY4MDMxNDQ0NDk0NTkxMjQ5/topshot-fbl-wc-2018-match64-fra-cro-5b4c8e9a42fc3353af000075jpg.jpg",
        team="France",
        year=2018,
        position="MF",
        value=5,
        tournament_id=2
    )

    p47 = Player (
        first_name="Olivier",
        last_name="Giroud",
        aka="Giroud",
        picture="https://digitalhub.fifa.com/m/2f3bbeb023837326/webimage-World-Cup-Champions-France-Portrait-Session-15-Jul-2018.png",
        team="France",
        year=2018,
        position="FW",
        value=5,
        tournament_id=2
    )

    p48 = Player (
        first_name="Kylian",
        last_name="Mbappé",
        aka="Mbappé",
        picture="https://www.telegraph.co.uk/content/dam/world-cup/2018/07/15/TELEMMGLPICT000169493493_trans_NvBQzQNjv4BqLeUJvOJqnV613e1NxllMSYIixnj0N-lTmS4HQcSqwKA.jpeg",
        team="France",
        year=2018,
        position="FW",
        value=11,
        tournament_id=2
    )

    p49 = Player (
        first_name="Antoine",
        last_name="Griezmann",
        aka="Griezmann",
        picture="https://pbs.twimg.com/media/DiKl3gIX4AAzcaD?format=jpg&name=4096x4096",
        team="France",
        year=2018,
        position="FW",
        value=13,
        tournament_id=2
    )

    # ITALY 2006

    p50 = Player (
        first_name="Gianluigi",
        last_name="Buffon",
        aka="Buffon",
        picture="https://ichef.bbci.co.uk/images/ic/1920x1080/p067n1sc.jpg",
        team="Italy",
        year=2006,
        position="GK",
        value=6,
        tournament_id=5
    )

    p51 = Player (
        first_name="Gianluca",
        last_name="Zambrotta",
        aka="Zambrotta",
        picture="https://worldfootballindex.com/wp-content/uploads/2020/03/gianluca-zambrotta.jpg",
        team="Italy",
        year=2006,
        position="DF",
        value=5,
        tournament_id=5
    )

    p52 = Player (
        first_name="Fabio",
        last_name="Grosso",
        aka="Grosso",
        picture="https://storage.googleapis.com/afs-prod/media/570cf874393144188cf0c65e81a283d2/3000.jpeg",
        team="Italy",
        year=2006,
        position="DF",
        value=5,
        tournament_id=5
    )

    p53 = Player (
        first_name="Fabio",
        last_name="Cannavaro",
        aka="Cannavaro",
        picture="https://sm.imgix.net/14/19/fabio-cannavaro.jpg?w=640&h=480&auto=compress,format&fit=clip",
        team="Italy",
        year=2006,
        position="DF",
        value=5,
        tournament_id=5
    )

    p54 = Player (
        first_name="Marco",
        last_name="Materazzi",
        aka="Materazzi",
        picture="https://content.api.news/v3/images/bin/b1aa8a1c57e272196a35a0ffcbd429a2",
        team="Italy",
        year=2006,
        position="DF",
        value=5,
        tournament_id=5
    )

    p55 = Player (
        first_name="Gennaro",
        last_name="Gattuso",
        aka="Gattuso",
        picture="https://pbs.twimg.com/media/ExGI3KHXAAUzQKI?format=jpg&name=4096x4096",
        team="Italy",
        year=2006,
        position="MF",
        value=5,
        tournament_id=5
    )

    p56 = Player (
        first_name="Andrea",
        last_name="Pirlo",
        aka="Pirlo",
        picture="https://ichef.bbci.co.uk/images/ic/1920x1080/p05m62f4.jpg",
        team="Italy",
        year=2006,
        position="MF",
        value=5,
        tournament_id=5
    )

    p57 = Player (
        first_name="Francesco",
        last_name="Totti",
        aka="Totti",
        picture="https://d3lbfr570u7hdr.cloudfront.net/stadiumastro/media/perform-article/2022/nov/18/francesco-totti_a8krog3voc1416uyfshrkdjsx.jpg",
        team="Italy",
        year=2006,
        position="FW",
        value=5,
        tournament_id=5
    )

    p58 = Player (
        first_name="Luca",
        last_name="Toni",
        aka="Toni",
        picture="https://d3nfwcxd527z59.cloudfront.net/content/uploads/2020/11/15122720/luca-toni-italy.jpg",
        team="Italy",
        year=2006,
        position="FW",
        value=5,
        tournament_id=5
    )

    p59 = Player (
        first_name="Alessandro",
        last_name="Del Piero",
        aka="Del Piero",
        picture="https://digitalhub.fifa.com/transform/6bab80b6-30ba-4ad7-9bf8-0231b0117ce3/2006_SF_GER_ITA_Del_Piero_120-1",
        team="Italy",
        year=2006,
        position="FW",
        value=5,
        tournament_id=5
    )

    p60 = Player (
        first_name="Zinedine",
        last_name="Zidane",
        aka="Zidane",
        picture="https://i.guim.co.uk/img/media/f02d99c0c61e788e3b293f24b7c0872233e70252/0_23_2640_1584/master/2640.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=4b50e9068e2865bc5bcd3e3204e75307",
        team="France",
        year=2006,
        position="MF",
        value=5,
        tournament_id=5
    )

    p61 = Player (
        first_name="Marcos",
        last_name="Roberto",
        aka="Marcos",
        picture="https://www.thesun.co.uk/wp-content/uploads/2022/06/NINTCHDBPICT000001881515.jpg",
        team="Brazil",
        year=2002,
        position="GK",
        value=5,
        tournament_id=6
    )

    p62 = Player (
        first_name="Marcos",
        last_name="Cafu",
        aka="Cafu",
        picture="https://tmssl.akamaized.net/images/foto/galerie/cafu-mit-dem-wm-pokal-1589276246-38312.jpg?lm=1589276306",
        team="Brazil",
        year=2002,
        position="DF",
        value=5,
        tournament_id=6
    )

    p63 = Player (
        first_name="Roberto",
        last_name="Carlos",
        aka="R. Carlos",
        picture="https://d3nfwcxd527z59.cloudfront.net/content/uploads/2020/06/13121742/Roberto-Carlos-Brazil-celebrates.jpg",
        team="Brazil",
        year=2002,
        position="DF",
        value=5,
        tournament_id=6
    )

    p64 = Player (
        first_name="José",
        last_name="Edmílson",
        aka="Edmílson",
        picture="https://i.guim.co.uk/img/media/5df144ea612c25aebdad9138db3f9b8dcc19046c/0_133_2356_1415/master/2356.jpg?width=1200&height=900&quality=85&auto=format&fit=crop&s=0b8d98b795bb07f25a0af28947e877d1",
        team="Brazil",
        year=2002,
        position="DF",
        value=5,
        tournament_id=6
    )

    p65 = Player (
        first_name="Lúcio",
        last_name="da Silva",
        aka="Lúcio",
        picture="https://ronaldo.com/wp-content/uploads/2019/06/GettyImages-88729456.jpg",
        team="Brazil",
        year=2002,
        position="DF",
        value=5,
        tournament_id=6
    )

    p66 = Player (
        first_name="Roque",
        last_name="Júnior",
        aka="Roque .J",
        picture="https://editorial01.shutterstock.com/preview-440/7434185ab/df88968a/Shutterstock_7434185ab.jpg",
        team="Brazil",
        year=2002,
        position="DF",
        value=5,
        tournament_id=6
    )

    p67 = Player (
        first_name="Gilberto",
        last_name="Silva",
        aka="G. Silva",
        picture="https://images.beinsports.com/Q9_taZrBVESYf3o9pMLnxD8QbtY=/full-fit-in/1000x0/gilbertosilva-cropped_nzn8ij22jpvw1i2ov5s5gyabx.jpg",
        team="Brazil",
        year=2002,
        position="MF",
        value=5,
        tournament_id=6
    )

    p68 = Player (
        first_name="Juninho",
        last_name="Paulista",
        aka="Juninho",
        picture="https://i0.wp.com/thesefootballtimes.co/wp-content/uploads/2018/01/juninho.jpg?fit=1600%2C1046&ssl=1",
        team="Brazil",
        year=2002,
        position="MF",
        value=5,
        tournament_id=6
    )

    p69 = Player (
        first_name="Ronaldinho",
        last_name="Gaúcho",
        aka="Ronaldinho",
        picture="http://ronaldinho7.weebly.com/uploads/3/8/7/9/38795437/5508042_orig.jpg",
        team="Brazil",
        year=2002,
        position="MF",
        value=5,
        tournament_id=6
    )

    p70 = Player (
        first_name="Rivaldo",
        last_name="Ferreira",
        aka="Rivaldo",
        picture="https://cdn.sportscroll.com/wp-content/uploads/2019/06/rivaldo-1.jpg",
        team="Brazil",
        year=2002,
        position="FW",
        value=5,
        tournament_id=6
    )

    p71 = Player (
        first_name="Miroslav",
        last_name="Klose",
        aka="Klose",
        picture="https://digitalhub.fifa.com/transform/eeaa504b-fefd-4f29-8583-bc3fcd521984/2002_E_Klose_1-0_GER_IRL",
        team="Germany",
        year=2002,
        position="FW",
        value=5,
        tournament_id=6
    )

    p72 = Player (
        first_name="Miroslav",
        last_name="Klose",
        aka="Klose",
        picture="https://footballwhispers.com/wp-content/uploads/2018/05/Klose-2006.jpg",
        team="Germany",
        year=2006,
        position="FW",
        value=5,
        tournament_id=5
    )

    p73 = Player (
        first_name="Michael",
        last_name="Ballack",
        aka="Ballack",
        picture="https://pbs.twimg.com/media/Dgs53G8WAAEERYJ.jpg:large",
        team="Germany",
        year=2002,
        position="MF",
        value=5,
        tournament_id=6
    )

    p74 = Player (
        first_name="Oliver",
        last_name="Kahn",
        aka="Kahn",
        picture="https://digitalhub.fifa.com/transform/33f6020c-56f5-42d3-8ad8-cc93696910df/2002_KAHN_LEV_YASHIN_AWARD",
        team="Germany",
        year=2002,
        position="GK",
        value=5,
        tournament_id=6
    )

    p75 = Player (
        first_name="Kylian",
        last_name="Mbappé",
        aka="Mbappé",
        picture="https://cdn.theathletic.com/app/uploads/2022/12/18131832/GettyImages-1450089040-scaled.jpg",
        team="France",
        year=2022,
        position="FW",
        value=12,
        tournament_id=1
    )

    p76 = Player (
        first_name="Harry",
        last_name="Kane",
        aka="Kane",
        picture="https://img.asmedia.epimg.net/resizer/OdAMoOUIuQZ4NjPcX4q-r56uhv4=/1952x1098/cloudfront-eu-central-1.images.arcpublishing.com/diarioas/D2D2NPAMOZKDRH5MKPO5VSZCXA.jpg",
        team="France",
        year=2018,
        position="FW",
        value=9,
        tournament_id=2
    )

    p77 = Player (
        first_name="Luka",
        last_name="Modrić",
        aka="Modrić",
        picture="https://images.beinsports.com/iCAahhEnsFbEas3rN5FBhUvAc-c=/1300x731/smart/luka-modric-cropped_1x53vmftwlb6r1gynsc48i0yb1.jpg",
        team="Croatia",
        year=2018,
        position="MF",
        value=5,
        tournament_id=2
    )

    p78 = Player (
        first_name="Lionel",
        last_name="Messi",
        aka="Messi",
        picture="https://e0.365dm.com/14/06/2048x1152/football-2014-fifa-world-cup-fifa-world-cup-2014-world-cup-fifa-world-cup-nigeria_3163800.jpg",
        team="Argentina",
        year=2014,
        position="FW",
        value=5,
        tournament_id=3
    )

    p79 = Player (
        first_name="Thomas",
        last_name="Müller",
        aka="Müller",
        picture="https://live.staticflickr.com/4139/4781090703_0e27e718df_z.jpg",
        team="Germany",
        year=2010,
        position="FW",
        value=5,
        tournament_id=4
    )

    p80 = Player (
        first_name="Diego",
        last_name="Forlán",
        aka="Forlán",
        picture="https://pbs.twimg.com/media/B_3PNzcUYAAjERW?format=jpg&name=4096x4096",
        team="Uruguay",
        year=2010,
        position="FW",
        value=5,
        tournament_id=4
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
            p28,
            p29,
            p30,
            p31,
            p32,
            p33,
            p34,
            p35,
            p36,
            p37,
            p38,
            p39,
            p40,
            p41,
            p42,
            p43,
            p44,
            p45,
            p46,
            p47,
            p48,
            p49,
            p50,
            p51,
            p52,
            p53,
            p54,
            p55,
            p56,
            p57,
            p58,
            p59,
            p60,
            p61,
            p62,
            p63,
            p64,
            p65,
            p66,
            p67,
            p68,
            p69,
            p70,
            p71,
            p72,
            p73,
            p74,
            p75,
            p76,
            p77,
            p78,
            p79,
            p80
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
