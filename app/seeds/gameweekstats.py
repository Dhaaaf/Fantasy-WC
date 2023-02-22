from app.models import db, GameWeekStat, environment, SCHEMA


def seed_game_week_stats():

    # ARGENTINA WC 2022 STATS
    gw1 = GameWeekStat (
        week=1,
        player_id=1,
        points=6,
        goals=1,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw2 = GameWeekStat (
        week=1,
        player_id=2,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw3 = GameWeekStat (
        week=1,
        player_id=3,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw4 = GameWeekStat (
        week=1,
        player_id=4,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw5 = GameWeekStat (
        week=1,
        player_id=5,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw6 = GameWeekStat (
        week=1,
        player_id=6,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw7 = GameWeekStat (
        week=1,
        player_id=7,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw8 = GameWeekStat (
        week=1,
        player_id=8,
        points=0,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw9 = GameWeekStat (
        week=1,
        player_id=9,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw10 = GameWeekStat (
        week=1,
        player_id=10,
        points=5,
        goals=0,
        assists=1,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw11 = GameWeekStat (
        week=1,
        player_id=11,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw12 = GameWeekStat (
        week=1,
        player_id=12,
        points=0,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw13 = GameWeekStat (
        week=1,
        player_id=13,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw14 = GameWeekStat (
        week=1,
        player_id=14,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw15 = GameWeekStat (
        week=2,
        player_id=1,
        points=15,
        goals=1,
        assists=1,
        clean_sheet=True,
        man_of_the_match=True,
    )

    gw16 = GameWeekStat (
        week=2,
        player_id=2,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw17 = GameWeekStat (
        week=2,
        player_id=3,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw18 = GameWeekStat (
        week=2,
        player_id=4,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw19 = GameWeekStat (
        week=2,
        player_id=5,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw20 = GameWeekStat (
        week=2,
        player_id=6,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw21 = GameWeekStat (
        week=2,
        player_id=7,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw22 = GameWeekStat (
        week=2,
        player_id=8,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw23 = GameWeekStat (
        week=2,
        player_id=9,
        points=6,
        goals=0,
        assists=1,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw24 = GameWeekStat (
        week=2,
        player_id=10,
        points=0,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw25 = GameWeekStat (
        week=2,
        player_id=11,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw26 = GameWeekStat (
        week=2,
        player_id=12,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw27 = GameWeekStat (
        week=2,
        player_id=13,
        points=8,
        goals=1,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw28 = GameWeekStat (
        week=2,
        player_id=14,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw29 = GameWeekStat (
        week=3,
        player_id=1,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw30 = GameWeekStat (
        week=3,
        player_id=2,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw31 = GameWeekStat (
        week=3,
        player_id=3,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw32 = GameWeekStat (
        week=3,
        player_id=4,
        points=0,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw33 = GameWeekStat (
        week=3,
        player_id=5,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw34 = GameWeekStat (
        week=3,
        player_id=6,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw35 = GameWeekStat (
        week=3,
        player_id=7,
        points=9,
        goals=0,
        assists=1,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw36 = GameWeekStat (
        week=3,
        player_id=8,
        points=0,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw37 = GameWeekStat (
        week=3,
        player_id=9,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw38 = GameWeekStat (
        week=3,
        player_id=10,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw39 = GameWeekStat (
        week=3,
        player_id=11,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw40 = GameWeekStat (
        week=3,
        player_id=12,
        points=13,
        goals=1,
        assists=0,
        clean_sheet=True,
        man_of_the_match=True,
    )

    gw41 = GameWeekStat (
        week=3,
        player_id=13,
        points=6,
        goals=0,
        assists=1,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw42 = GameWeekStat (
        week=3,
        player_id=14,
        points=6,
        goals=1,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw43 = GameWeekStat (
        week=4,
        player_id=1,
        points=12,
        goals=1,
        assists=0,
        clean_sheet=False,
        man_of_the_match=True,
    )

    gw44 = GameWeekStat (
        week=4,
        player_id=2,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw45 = GameWeekStat (
        week=4,
        player_id=3,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw46 = GameWeekStat (
        week=4,
        player_id=4,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw47 = GameWeekStat (
        week=4,
        player_id=5,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw48 = GameWeekStat (
        week=4,
        player_id=6,
        points=5,
        goals=0,
        assists=1,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw49 = GameWeekStat (
        week=4,
        player_id=7,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw50 = GameWeekStat (
        week=4,
        player_id=8,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw51 = GameWeekStat (
        week=4,
        player_id=9,
        points=0,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw52 = GameWeekStat (
        week=4,
        player_id=10,
        points=0,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw53 = GameWeekStat (
        week=4,
        player_id=11,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw54 = GameWeekStat (
        week=4,
        player_id=12,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw55 = GameWeekStat (
        week=4,
        player_id=13,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw56 = GameWeekStat (
        week=4,
        player_id=14,
        points=6,
        goals=1,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw57 = GameWeekStat (
        week=5,
        player_id=1,
        points=15,
        goals=1,
        assists=1,
        clean_sheet=False,
        man_of_the_match=True,
    )

    gw58 = GameWeekStat (
        week=5,
        player_id=2,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw59 = GameWeekStat (
        week=5,
        player_id=3,
        points=5,
        goals=0,
        assists=1,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw60 = GameWeekStat (
        week=5,
        player_id=4,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw61 = GameWeekStat (
        week=5,
        player_id=5,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw62 = GameWeekStat (
        week=5,
        player_id=6,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw63 = GameWeekStat (
        week=5,
        player_id=7,
        points=8,
        goals=1,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw64 = GameWeekStat (
        week=5,
        player_id=8,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw65 = GameWeekStat (
        week=5,
        player_id=9,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw66 = GameWeekStat (
        week=5,
        player_id=10,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw67 = GameWeekStat (
        week=5,
        player_id=11,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw68 = GameWeekStat (
        week=5,
        player_id=12,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw69 = GameWeekStat (
        week=5,
        player_id=13,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw70 = GameWeekStat (
        week=5,
        player_id=14,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw71 = GameWeekStat (
        week=6,
        player_id=1,
        points=15,
        goals=1,
        assists=1,
        clean_sheet=True,
        man_of_the_match=True,
    )

    gw72 = GameWeekStat (
        week=6,
        player_id=2,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw73 = GameWeekStat (
        week=6,
        player_id=3,
        points=0,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw74 = GameWeekStat (
        week=6,
        player_id=4,
        points=0,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw75 = GameWeekStat (
        week=6,
        player_id=5,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw76 = GameWeekStat (
        week=6,
        player_id=6,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw77 = GameWeekStat (
        week=6,
        player_id=7,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw78 = GameWeekStat (
        week=6,
        player_id=8,
        points=0,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw79 = GameWeekStat (
        week=6,
        player_id=9,
        points=0,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw80 = GameWeekStat (
        week=6,
        player_id=10,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw81 = GameWeekStat (
        week=6,
        player_id=11,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw82 = GameWeekStat (
        week=6,
        player_id=12,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw83 = GameWeekStat (
        week=6,
        player_id=13,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw84 = GameWeekStat (
        week=6,
        player_id=14,
        points=13,
        goals=2,
        assists=1,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw85 = GameWeekStat (
        week=7,
        player_id=1,
        points=16,
        goals=2,
        assists=0,
        clean_sheet=False,
        man_of_the_match=True,
    )

    gw86 = GameWeekStat (
        week=7,
        player_id=2,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw87 = GameWeekStat (
        week=7,
        player_id=3,
        points=5,
        goals=0,
        assists=1,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw88 = GameWeekStat (
        week=7,
        player_id=4,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw89 = GameWeekStat (
        week=7,
        player_id=5,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw90 = GameWeekStat (
        week=7,
        player_id=6,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw91 = GameWeekStat (
        week=7,
        player_id=7,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw92 = GameWeekStat (
        week=7,
        player_id=8,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw93 = GameWeekStat (
        week=7,
        player_id=9,
        points=11,
        goals=1,
        assists=1,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw94 = GameWeekStat (
        week=7,
        player_id=10,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw95 = GameWeekStat (
        week=7,
        player_id=11,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw96 = GameWeekStat (
        week=7,
        player_id=12,
        points=5,
        goals=0,
        assists=1,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw97 = GameWeekStat (
        week=7,
        player_id=13,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw98 = GameWeekStat (
        week=7,
        player_id=14,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    # RONALDO NAZARIO R9 WC 2002

    gw99 = GameWeekStat (
        week=1,
        player_id=15,
        points=6,
        goals=1,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw100 = GameWeekStat (
        week=2,
        player_id=15,
        points=9,
        goals=1,
        assists=1,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw101 = GameWeekStat (
        week=3,
        player_id=15,
        points=16,
        goals=2,
        assists=0,
        clean_sheet=False,
        man_of_the_match=True,
    )

    gw102 = GameWeekStat (
        week=4,
        player_id=15,
        points=6,
        goals=1,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw103 = GameWeekStat (
        week=5,
        player_id=15,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw104 = GameWeekStat (
        week=6,
        player_id=15,
        points=6,
        goals=1,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw105 = GameWeekStat (
        week=7,
        player_id=15,
        points=16,
        goals=2,
        assists=0,
        clean_sheet=True,
        man_of_the_match=True,
    )

    gw106 = GameWeekStat (
        week=1,
        player_id=16,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw107 = GameWeekStat (
        week=2,
        player_id=16,
        points=14,
        goals=1,
        assists=0,
        clean_sheet=True,
        man_of_the_match=True,
    )

    gw108 = GameWeekStat (
        week=3,
        player_id=16,
        points=5,
        goals=1,
        assists=1,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw109 = GameWeekStat (
        week=4,
        player_id=16,
        points=13,
        goals=1,
        assists=0,
        clean_sheet=False,
        man_of_the_match=True,
    )

    gw110 = GameWeekStat (
        week=5,
        player_id=16,
        points=13,
        goals=1,
        assists=0,
        clean_sheet=False,
        man_of_the_match=True,
    )

    gw111 = GameWeekStat (
        week=6,
        player_id=16,
        points=13,
        goals=1,
        assists=0,
        clean_sheet=False,
        man_of_the_match=True,
    )

    gw112 = GameWeekStat (
        week=6,
        player_id=16,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )


    db.session.add_all(
        [
            gw1,
            gw2,
            gw3,
            gw4,
            gw5,
            gw6,
            gw7,
            gw8,
            gw9,
            gw10,
            gw11,
            gw12,
            gw13,
            gw14,
            gw15,
            gw16,
            gw17,
            gw18,
            gw19,
            gw20,
            gw21,
            gw22,
            gw23,
            gw24,
            gw25,
            gw26,
            gw27,
            gw28,
            gw29,
            gw30,
            gw31,
            gw32,
            gw33,
            gw34,
            gw35,
            gw36,
            gw37,
            gw38,
            gw39,
            gw40,
            gw41,
            gw42,
            gw43,
            gw44,
            gw45,
            gw46,
            gw47,
            gw48,
            gw49,
            gw50,
            gw51,
            gw52,
            gw53,
            gw54,
            gw55,
            gw56,
            gw57,
            gw58,
            gw59,
            gw60,
            gw61,
            gw62,
            gw63,
            gw64,
            gw65,
            gw66,
            gw67,
            gw68,
            gw69,
            gw70,
            gw71,
            gw72,
            gw73,
            gw74,
            gw75,
            gw76,
            gw77,
            gw78,
            gw79,
            gw80,
            gw81,
            gw82,
            gw83,
            gw84,
            gw85,
            gw86,
            gw87,
            gw88,
            gw89,
            gw90,
            gw91,
            gw92,
            gw93,
            gw94,
            gw95,
            gw96,
            gw97,
            gw98,
            gw99,
            gw100,
            gw101,
            gw102,
            gw103,
            gw104,
            gw105,
            gw106,
            gw107,
            gw108,
            gw109,
            gw110,
            gw111,
            gw112
        ]
    )
    db.session.commit()


def undo_game_week_stats():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.game_week_stats_table RESTART IDENTITY CASCADE;"
        )
    else:
        db.session.execute("DELETE FROM game_week_stats_table")

    db.session.commit()
