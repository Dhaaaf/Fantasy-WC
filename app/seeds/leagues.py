from app.models import db, League, environment, SCHEMA


def seed_leagues():

    l1 = League (
        owner_id =2,
        name ="All or Nothing",
        display_pic ="https://www.ipsos.com/sites/default/files/styles/max_1300x1300/public/ct/news_and_polls/2022-11/ipsos-global-advisor-fifa-world-cup-2022.jpg?itok=G7HtaVZa",
        team_budget=100,
        is_private=False
    )

    l2 = League (
        owner_id =1,
        name ="Old is Gold",
        display_pic ="https://i2-prod.mirror.co.uk/incoming/article25415910.ece/ALTERNATES/s1200c/0_GettyImages-88019502.jpg",
        team_budget=130,
        is_private=False
    )

    l3 = League (
        owner_id =3,
        name ="One more try",
        display_pic ="https://images.adsttc.com/media/images/6334/0bcc/7120/024a/58db/cbe1/large_jpg/qatars-lusail-stadium-designed-by-foster-plus-partners-hosts-its-first-game_7.jpg?1664355284",
        team_budget=110,
        is_private=False
    )

    l4 = League (
        owner_id =1,
        name ="Fergie Time",
        display_pic ="https://assets.goal.com/v3/assets/bltcc7a7ffd2fbf71f5/blt261e76ddd443705f/60db777390ef0d39a2fd978e/f5acbb2cbc63eed78904048af649b4ca44e0db23.png?auto=webp&fit=crop&format=jpg&height=800&quality=60&width=1200",
        team_budget=93,
        is_private=True
    )

    l5 = League (
        owner_id =2,
        name ="Money League",
        display_pic ="https://media.licdn.com/dms/image/C5112AQFj4FT9bK_p7w/article-cover_image-shrink_600_2000/0/1563191183154?e=2147483647&v=beta&t=emmTP6DImh71L4CWQy2X-wryBvdwROCqplBK0f2wG8Q",
        team_budget=200,
        is_private=True
    )

    db.session.add_all(
        [
            l1,
            l2,
            l3,
            l4,
            l5,
        ]
    )
    db.session.commit()






def undo_leagues():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.leagues_table RESTART IDENTITY CASCADE;"
        )
    else:
        db.session.execute("DELETE FROM leagues_table")

    db.session.commit()
