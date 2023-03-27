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
        points=2,
        goals=0,
        assists=0,
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
        points=10,
        goals=2,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
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
        points=12,
        goals=1,
        assists=0,
        clean_sheet=True,
        man_of_the_match=True,
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

    # Wesley Sneijder 2010

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
        goals=0,
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
        points=18,
        goals=2,
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
        week=7,
        player_id=16,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    # Manuel Neuer 2014

    gw113 = GameWeekStat (
        week=1,
        player_id=17,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw114 = GameWeekStat (
        week=2,
        player_id=17,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw115 = GameWeekStat (
        week=3,
        player_id=17,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw116 = GameWeekStat (
        week=4,
        player_id=17,
        points=8,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=True,
    )

    gw117 = GameWeekStat (
        week=5,
        player_id=17,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw118 = GameWeekStat (
        week=6,
        player_id=17,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw119 = GameWeekStat (
        week=7,
        player_id=17,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    # Howedes 2014

    gw120 = GameWeekStat (
        week=1,
        player_id=18,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw121 = GameWeekStat (
        week=2,
        player_id=18,
        points=5,
        goals=0,
        assists=1,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw122 = GameWeekStat (
        week=3,
        player_id=18,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw123 = GameWeekStat (
        week=4,
        player_id=18,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw124 = GameWeekStat (
        week=5,
        player_id=18,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw125 = GameWeekStat (
        week=6,
        player_id=18,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw126 = GameWeekStat (
        week=7,
        player_id=18,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    # Mats Hummels - 2014

    gw127 = GameWeekStat (
        week=1,
        player_id=19,
        points=12,
        goals=1,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw128 = GameWeekStat (
        week=2,
        player_id=19,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw129 = GameWeekStat (
        week=3,
        player_id=19,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw130 = GameWeekStat (
        week=4,
        player_id=19,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw131 = GameWeekStat (
        week=5,
        player_id=19,
        points=18,
        goals=1,
        assists=0,
        clean_sheet=True,
        man_of_the_match=True,
    )

    gw132 = GameWeekStat (
        week=6,
        player_id=19,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw133 = GameWeekStat (
        week=7,
        player_id=19,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    # Jerome Boateng 2014

    gw134 = GameWeekStat (
        week=1,
        player_id=20,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw135 = GameWeekStat (
        week=2,
        player_id=20,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw136 = GameWeekStat (
        week=3,
        player_id=20,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw137 = GameWeekStat (
        week=4,
        player_id=20,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw138 = GameWeekStat (
        week=5,
        player_id=20,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw139 = GameWeekStat (
        week=6,
        player_id=20,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw140 = GameWeekStat (
        week=7,
        player_id=20,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    # Philipp Lahm 2014

    gw141 = GameWeekStat (
        week=1,
        player_id=21,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw142 = GameWeekStat (
        week=2,
        player_id=21,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw143 = GameWeekStat (
        week=3,
        player_id=21,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw144 = GameWeekStat (
        week=4,
        player_id=21,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw145 = GameWeekStat (
        week=5,
        player_id=21,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw146 = GameWeekStat (
        week=6,
        player_id=21,
        points=8,
        goals=0,
        assists=2,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw147 = GameWeekStat (
        week=7,
        player_id=21,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    # Sami Khedira 2014

    gw148 = GameWeekStat (
        week=1,
        player_id=22,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw149 = GameWeekStat (
        week=2,
        player_id=22,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw150 = GameWeekStat (
        week=3,
        player_id=22,
        points=0,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw151 = GameWeekStat (
        week=4,
        player_id=22,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw152 = GameWeekStat (
        week=5,
        player_id=22,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw153 = GameWeekStat (
        week=6,
        player_id=22,
        points=10,
        goals=1,
        assists=1,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw154 = GameWeekStat (
        week=7,
        player_id=22,
        points=0,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    # Mesut Ozil 2014

    gw155 = GameWeekStat (
        week=1,
        player_id=23,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw156 = GameWeekStat (
        week=2,
        player_id=23,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw157 = GameWeekStat (
        week=3,
        player_id=23,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw158 = GameWeekStat (
        week=4,
        player_id=23,
        points=7,
        goals=1,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw159 = GameWeekStat (
        week=5,
        player_id=23,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw160 = GameWeekStat (
        week=6,
        player_id=23,
        points=5,
        goals=0,
        assists=1,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw161 = GameWeekStat (
        week=7,
        player_id=23,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    # Andre Schurrle 2014

    gw162 = GameWeekStat (
        week=1,
        player_id=24,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw163 = GameWeekStat (
        week=2,
        player_id=24,
        points=0,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw164 = GameWeekStat (
        week=3,
        player_id=24,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw165 = GameWeekStat (
        week=4,
        player_id=24,
        points=7,
        goals=1,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw166 = GameWeekStat (
        week=5,
        player_id=24,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw167 = GameWeekStat (
        week=6,
        player_id=24,
        points=12,
        goals=2,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw168 = GameWeekStat (
        week=7,
        player_id=24,
        points=6,
        goals=0,
        assists=1,
        clean_sheet=True,
        man_of_the_match=False,
    )

    # Mario Gotze

    gw169 = GameWeekStat (
        week=1,
        player_id=25,
        points=5,
        goals=0,
        assists=1,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw170 = GameWeekStat (
        week=2,
        player_id=25,
        points=7,
        goals=1,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw171 = GameWeekStat (
        week=3,
        player_id=25,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw172 = GameWeekStat (
        week=4,
        player_id=25,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw173 = GameWeekStat (
        week=5,
        player_id=25,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw174 = GameWeekStat (
        week=6,
        player_id=25,
        points=0,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw175 = GameWeekStat (
        week=7,
        player_id=25,
        points=14,
        goals=1,
        assists=0,
        clean_sheet=True,
        man_of_the_match=True,
    )

    # Toni Kroos 2014

    gw176 = GameWeekStat (
        week=1,
        player_id=26,
        points=9,
        goals=0,
        assists=2,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw177 = GameWeekStat (
        week=2,
        player_id=26,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw178 = GameWeekStat (
        week=3,
        player_id=26,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw179 = GameWeekStat (
        week=4,
        player_id=26,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw180 = GameWeekStat (
        week=5,
        player_id=26,
        points=6,
        goals=0,
        assists=1,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw181 = GameWeekStat (
        week=6,
        player_id=26,
        points=21,
        goals=2,
        assists=1,
        clean_sheet=False,
        man_of_the_match=True,
    )

    gw182 = GameWeekStat (
        week=7,
        player_id=26,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    # Thomas Muller - 2014

    gw183 = GameWeekStat (
        week=1,
        player_id=27,
        points=20,
        goals=3,
        assists=0,
        clean_sheet=True,
        man_of_the_match=True,
    )

    gw184 = GameWeekStat (
        week=2,
        player_id=27,
        points=5,
        goals=0,
        assists=1,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw185 = GameWeekStat (
        week=3,
        player_id=27,
        points=12,
        goals=1,
        assists=0,
        clean_sheet=True,
        man_of_the_match=True,
    )

    gw186 = GameWeekStat (
        week=4,
        player_id=27,
        points=5,
        goals=0,
        assists=1,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw187 = GameWeekStat (
        week=5,
        player_id=27,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw188 = GameWeekStat (
        week=6,
        player_id=27,
        points=9,
        goals=1,
        assists=1,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw189 = GameWeekStat (
        week=7,
        player_id=27,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    # Mirolsav Klose - 2014

    gw190 = GameWeekStat (
        week=1,
        player_id=28,
        points=0,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw191 = GameWeekStat (
        week=2,
        player_id=28,
        points=6,
        goals=1,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw192 = GameWeekStat (
        week=3,
        player_id=28,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw193 = GameWeekStat (
        week=4,
        player_id=28,
        points=0,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw194 = GameWeekStat (
        week=5,
        player_id=28,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw195 = GameWeekStat (
        week=6,
        player_id=28,
        points=6,
        goals=1,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw196 = GameWeekStat (
        week=7,
        player_id=28,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    # SPAIN 2010

    # IKER CASILLAS

    gw197 = GameWeekStat (
        week=1,
        player_id=29,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw198 = GameWeekStat (
        week=2,
        player_id=29,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw199 = GameWeekStat (
        week=3,
        player_id=29,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw200 = GameWeekStat (
        week=4,
        player_id=29,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw201 = GameWeekStat (
        week=5,
        player_id=29,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw202 = GameWeekStat (
        week=6,
        player_id=29,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw203 = GameWeekStat (
        week=7,
        player_id=29,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    # Gerard Pique

    gw204 = GameWeekStat (
        week=1,
        player_id=30,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw205 = GameWeekStat (
        week=2,
        player_id=30,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw206 = GameWeekStat (
        week=3,
        player_id=30,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw207 = GameWeekStat (
        week=4,
        player_id=30,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw208 = GameWeekStat (
        week=5,
        player_id=30,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw209 = GameWeekStat (
        week=6,
        player_id=30,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw210 = GameWeekStat (
        week=7,
        player_id=30,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    # Sergio Ramos

    gw211 = GameWeekStat (
        week=1,
        player_id=31,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw212 = GameWeekStat (
        week=2,
        player_id=31,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw213 = GameWeekStat (
        week=3,
        player_id=31,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw214 = GameWeekStat (
        week=4,
        player_id=31,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw215 = GameWeekStat (
        week=5,
        player_id=31,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw216 = GameWeekStat (
        week=6,
        player_id=31,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw217 = GameWeekStat (
        week=7,
        player_id=31,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    # Carles Puyol

    gw218 = GameWeekStat (
        week=1,
        player_id=32,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw219 = GameWeekStat (
        week=2,
        player_id=32,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw220 = GameWeekStat (
        week=3,
        player_id=32,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw221 = GameWeekStat (
        week=4,
        player_id=32,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw222 = GameWeekStat (
        week=5,
        player_id=32,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw223 = GameWeekStat (
        week=6,
        player_id=32,
        points=18,
        goals=1,
        assists=0,
        clean_sheet=True,
        man_of_the_match=True,
    )

    gw224 = GameWeekStat (
        week=7,
        player_id=32,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    # Sergio Busquets

    gw225 = GameWeekStat (
        week=1,
        player_id=33,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw226 = GameWeekStat (
        week=2,
        player_id=33,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw227 = GameWeekStat (
        week=3,
        player_id=33,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw228 = GameWeekStat (
        week=4,
        player_id=33,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw229 = GameWeekStat (
        week=5,
        player_id=33,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw230 = GameWeekStat (
        week=6,
        player_id=33,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw231 = GameWeekStat (
        week=7,
        player_id=33,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    # Xabi Alonso

    gw232 = GameWeekStat (
        week=1,
        player_id=34,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw233 = GameWeekStat (
        week=2,
        player_id=34,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw234 = GameWeekStat (
        week=3,
        player_id=34,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw235 = GameWeekStat (
        week=4,
        player_id=34,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw236 = GameWeekStat (
        week=5,
        player_id=34,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw237 = GameWeekStat (
        week=6,
        player_id=34,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw238 = GameWeekStat (
        week=7,
        player_id=34,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    # Cesc Fabregas

    gw239 = GameWeekStat (
        week=1,
        player_id=35,
        points=0,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw240 = GameWeekStat (
        week=2,
        player_id=35,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw241 = GameWeekStat (
        week=3,
        player_id=35,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw242 = GameWeekStat (
        week=4,
        player_id=35,
        points=0,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw243 = GameWeekStat (
        week=5,
        player_id=35,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw244 = GameWeekStat (
        week=6,
        player_id=35,
        points=0,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw245 = GameWeekStat (
        week=7,
        player_id=35,
        points=6,
        goals=0,
        assists=1,
        clean_sheet=True,
        man_of_the_match=False,
    )

    # Xavi Hernandez

    gw246 = GameWeekStat (
        week=1,
        player_id=36,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw247 = GameWeekStat (
        week=2,
        player_id=36,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw248 = GameWeekStat (
        week=3,
        player_id=36,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw249 = GameWeekStat (
        week=4,
        player_id=36,
        points=12,
        goals=0,
        assists=1,
        clean_sheet=True,
        man_of_the_match=True,
    )

    gw250 = GameWeekStat (
        week=5,
        player_id=36,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw251 = GameWeekStat (
        week=6,
        player_id=36,
        points=6,
        goals=0,
        assists=1,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw252 = GameWeekStat (
        week=7,
        player_id=36,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    # Andres Iniesta - 2010

    gw253 = GameWeekStat (
        week=1,
        player_id=37,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw254 = GameWeekStat (
        week=2,
        player_id=37,
        points=0,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw255 = GameWeekStat (
        week=3,
        player_id=37,
        points=13,
        goals=1,
        assists=0,
        clean_sheet=False,
        man_of_the_match=True,
    )

    gw256 = GameWeekStat (
        week=4,
        player_id=37,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw257 = GameWeekStat (
        week=5,
        player_id=37,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw258 = GameWeekStat (
        week=6,
        player_id=37,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw259 = GameWeekStat (
        week=7,
        player_id=37,
        points=14,
        goals=1,
        assists=0,
        clean_sheet=True,
        man_of_the_match=True,
    )

    # David Villa

    gw260 = GameWeekStat (
        week=1,
        player_id=38,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw261 = GameWeekStat (
        week=2,
        player_id=38,
        points=16,
        goals=2,
        assists=0,
        clean_sheet=True,
        man_of_the_match=True,
    )

    gw262 = GameWeekStat (
        week=3,
        player_id=38,
        points=9,
        goals=1,
        assists=1,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw263 = GameWeekStat (
        week=4,
        player_id=38,
        points=12,
        goals=1,
        assists=0,
        clean_sheet=True,
        man_of_the_match=True,
    )

    gw264 = GameWeekStat (
        week=5,
        player_id=38,
        points=6,
        goals=1,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw265 = GameWeekStat (
        week=6,
        player_id=38,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw266 = GameWeekStat (
        week=7,
        player_id=38,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    # Hugo Lloris 2018

    gw267 = GameWeekStat (
        week=1,
        player_id=39,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw268 = GameWeekStat (
        week=2,
        player_id=39,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw269 = GameWeekStat (
        week=3,
        player_id=39,
        points=0,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw270 = GameWeekStat (
        week=4,
        player_id=39,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw271 = GameWeekStat (
        week=5,
        player_id=39,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw272 = GameWeekStat (
        week=6,
        player_id=39,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw273 = GameWeekStat (
        week=7,
        player_id=39,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    # Lucas Hernandez 2018

    gw274 = GameWeekStat (
        week=1,
        player_id=40,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw275 = GameWeekStat (
        week=2,
        player_id=40,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw276 = GameWeekStat (
        week=3,
        player_id=40,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw277 = GameWeekStat (
        week=4,
        player_id=40,
        points=5,
        goals=0,
        assists=1,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw278 = GameWeekStat (
        week=5,
        player_id=40,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw279 = GameWeekStat (
        week=6,
        player_id=40,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw280 = GameWeekStat (
        week=7,
        player_id=40,
        points=5,
        goals=0,
        assists=1,
        clean_sheet=False,
        man_of_the_match=False,
    )

    # Benjamin Pavard 2018

    gw281 = GameWeekStat (
        week=1,
        player_id=41,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw282 = GameWeekStat (
        week=2,
        player_id=41,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw283 = GameWeekStat (
        week=3,
        player_id=41,
        points=0,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw284 = GameWeekStat (
        week=4,
        player_id=41,
        points=8,
        goals=1,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw285 = GameWeekStat (
        week=5,
        player_id=41,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw286 = GameWeekStat (
        week=6,
        player_id=41,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw287 = GameWeekStat (
        week=7,
        player_id=41,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    # Samuel Umtiti 2018


    gw288 = GameWeekStat (
        week=1,
        player_id=42,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw289 = GameWeekStat (
        week=2,
        player_id=42,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw290 = GameWeekStat (
        week=3,
        player_id=42,
        points=0,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw291 = GameWeekStat (
        week=4,
        player_id=42,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw292 = GameWeekStat (
        week=5,
        player_id=42,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw293 = GameWeekStat (
        week=6,
        player_id=42,
        points=18,
        goals=1,
        assists=0,
        clean_sheet=True,
        man_of_the_match=True,
    )

    gw294 = GameWeekStat (
        week=7,
        player_id=42,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    # Raphael Varane 2018

    gw295 = GameWeekStat (
        week=1,
        player_id=43,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw296 = GameWeekStat (
        week=2,
        player_id=43,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw297 = GameWeekStat (
        week=3,
        player_id=43,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw298 = GameWeekStat (
        week=4,
        player_id=43,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw299 = GameWeekStat (
        week=5,
        player_id=43,
        points=18,
        goals=1,
        assists=0,
        clean_sheet=True,
        man_of_the_match=True,
    )

    gw300 = GameWeekStat (
        week=6,
        player_id=43,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw301 = GameWeekStat (
        week=7,
        player_id=43,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    # Blaise Matuidi

    gw302 = GameWeekStat (
        week=1,
        player_id=44,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw303 = GameWeekStat (
        week=2,
        player_id=44,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw304 = GameWeekStat (
        week=3,
        player_id=44,
        points=0,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw305 = GameWeekStat (
        week=4,
        player_id=44,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw306 = GameWeekStat (
        week=5,
        player_id=44,
        points=0,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw307 = GameWeekStat (
        week=6,
        player_id=44,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw308 = GameWeekStat (
        week=7,
        player_id=44,
        points=5,
        goals=0,
        assists=1,
        clean_sheet=False,
        man_of_the_match=False,
    )

    # Ngolo Kante 2018

    gw309 = GameWeekStat (
        week=1,
        player_id=45,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw310 = GameWeekStat (
        week=2,
        player_id=45,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw311 = GameWeekStat (
        week=3,
        player_id=45,
        points=9,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=True,
    )

    gw312 = GameWeekStat (
        week=4,
        player_id=45,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw313 = GameWeekStat (
        week=5,
        player_id=45,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw314 = GameWeekStat (
        week=6,
        player_id=45,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw315 = GameWeekStat (
        week=7,
        player_id=45,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    # Paul Pogba

    gw316 = GameWeekStat (
        week=1,
        player_id=46,
        points=5,
        goals=0,
        assists=1,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw317 = GameWeekStat (
        week=2,
        player_id=46,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw318 = GameWeekStat (
        week=3,
        player_id=46,
        points=0,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw319 = GameWeekStat (
        week=4,
        player_id=46,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw320 = GameWeekStat (
        week=5,
        player_id=46,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw321 = GameWeekStat (
        week=6,
        player_id=46,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw322 = GameWeekStat (
        week=7,
        player_id=46,
        points=7,
        goals=1,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    # Olivier Giroud - 2018

    gw323 = GameWeekStat (
        week=1,
        player_id=47,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw324 = GameWeekStat (
        week=2,
        player_id=47,
        points=5,
        goals=0,
        assists=1,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw325 = GameWeekStat (
        week=3,
        player_id=47,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw326 = GameWeekStat (
        week=4,
        player_id=47,
        points=5,
        goals=0,
        assists=1,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw327 = GameWeekStat (
        week=5,
        player_id=47,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw328 = GameWeekStat (
        week=6,
        player_id=47,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw329 = GameWeekStat (
        week=7,
        player_id=47,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    # Kylian Mbappe - 2018

    gw330 = GameWeekStat (
        week=1,
        player_id=48,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw331 = GameWeekStat (
        week=2,
        player_id=48,
        points=12,
        goals=1,
        assists=0,
        clean_sheet=True,
        man_of_the_match=True,
    )

    gw332 = GameWeekStat (
        week=3,
        player_id=48,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw333 = GameWeekStat (
        week=4,
        player_id=48,
        points=19,
        goals=2,
        assists=1,
        clean_sheet=False,
        man_of_the_match=True,
    )

    gw334 = GameWeekStat (
        week=5,
        player_id=48,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw335 = GameWeekStat (
        week=6,
        player_id=48,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw336 = GameWeekStat (
        week=7,
        player_id=48,
        points=6,
        goals=1,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    # Antoine Griezmann 2018

    gw337 = GameWeekStat (
        week=1,
        player_id=49,
        points=12,
        goals=1,
        assists=0,
        clean_sheet=False,
        man_of_the_match=True,
    )

    gw338 = GameWeekStat (
        week=2,
        player_id=49,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw339 = GameWeekStat (
        week=3,
        player_id=49,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw340 = GameWeekStat (
        week=4,
        player_id=49,
        points=6,
        goals=1,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw341 = GameWeekStat (
        week=5,
        player_id=49,
        points=9,
        goals=1,
        assists=1,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw342 = GameWeekStat (
        week=6,
        player_id=49,
        points=5,
        goals=0,
        assists=1,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw343 = GameWeekStat (
        week=7,
        player_id=49,
        points=15,
        goals=1,
        assists=1,
        clean_sheet=False,
        man_of_the_match=True,
    )

    # Buffon - 2006

    gw344 = GameWeekStat (
        week=1,
        player_id=50,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw345 = GameWeekStat (
        week=2,
        player_id=50,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw346 = GameWeekStat (
        week=3,
        player_id=50,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw347 = GameWeekStat (
        week=4,
        player_id=50,
        points=12,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=True,
    )

    gw348 = GameWeekStat (
        week=5,
        player_id=50,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw349 = GameWeekStat (
        week=6,
        player_id=50,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw350 = GameWeekStat (
        week=7,
        player_id=50,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    # Zambrotta - 2006

    gw351 = GameWeekStat (
        week=1,
        player_id=51,
        points=0,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw352 = GameWeekStat (
        week=2,
        player_id=51,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw353 = GameWeekStat (
        week=3,
        player_id=51,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw354 = GameWeekStat (
        week=4,
        player_id=51,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw355 = GameWeekStat (
        week=5,
        player_id=51,
        points=15,
        goals=1,
        assists=1,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw356 = GameWeekStat (
        week=6,
        player_id=51,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw357 = GameWeekStat (
        week=7,
        player_id=51,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    # Fabio Grosso - 2006


    gw358 = GameWeekStat (
        week=1,
        player_id=52,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw359 = GameWeekStat (
        week=2,
        player_id=52,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw360 = GameWeekStat (
        week=3,
        player_id=52,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw361 = GameWeekStat (
        week=4,
        player_id=52,
        points=9,
        goals=0,
        assists=1,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw362 = GameWeekStat (
        week=5,
        player_id=52,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw363 = GameWeekStat (
        week=6,
        player_id=52,
        points=12,
        goals=1,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw364 = GameWeekStat (
        week=7,
        player_id=52,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    # Fabio Cannavaro - 2006

    gw365 = GameWeekStat (
        week=1,
        player_id=53,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw366 = GameWeekStat (
        week=2,
        player_id=53,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw367 = GameWeekStat (
        week=3,
        player_id=53,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw368 = GameWeekStat (
        week=4,
        player_id=53,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw369 = GameWeekStat (
        week=5,
        player_id=53,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw370 = GameWeekStat (
        week=6,
        player_id=53,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw371 = GameWeekStat (
        week=7,
        player_id=53,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    # Marco Materazzi 2006

    gw372 = GameWeekStat (
        week=1,
        player_id=54,
        points=0,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw373 = GameWeekStat (
        week=2,
        player_id=54,
        points=0,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw374 = GameWeekStat (
        week=3,
        player_id=54,
        points=12,
        goals=1,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw375 = GameWeekStat (
        week=4,
        player_id=54,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw376 = GameWeekStat (
        week=5,
        player_id=54,
        points=0,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw377 = GameWeekStat (
        week=6,
        player_id=54,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw378 = GameWeekStat (
        week=7,
        player_id=54,
        points=8,
        goals=1,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    # Gennaro Gattuso - 2006

    gw379 = GameWeekStat (
        week=1,
        player_id=55,
        points=0,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw380 = GameWeekStat (
        week=2,
        player_id=55,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw381 = GameWeekStat (
        week=3,
        player_id=55,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw382 = GameWeekStat (
        week=4,
        player_id=55,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw383 = GameWeekStat (
        week=5,
        player_id=55,
        points=9,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=True,
    )

    gw384 = GameWeekStat (
        week=6,
        player_id=55,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw385 = GameWeekStat (
        week=7,
        player_id=55,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    # Andrea Pirlo - 2006

    gw386 = GameWeekStat (
        week=1,
        player_id=56,
        points=14,
        goals=1,
        assists=0,
        clean_sheet=True,
        man_of_the_match=True,
    )

    gw387 = GameWeekStat (
        week=2,
        player_id=56,
        points=5,
        goals=0,
        assists=1,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw388 = GameWeekStat (
        week=3,
        player_id=56,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw389 = GameWeekStat (
        week=4,
        player_id=56,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw390 = GameWeekStat (
        week=5,
        player_id=56,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw391 = GameWeekStat (
        week=6,
        player_id=56,
        points=12,
        goals=0,
        assists=1,
        clean_sheet=True,
        man_of_the_match=True,
    )

    gw392 = GameWeekStat (
        week=7,
        player_id=56,
        points=11,
        goals=0,
        assists=1,
        clean_sheet=False,
        man_of_the_match=True,
    )

    # Francesco Totti - 2006

    gw393 = GameWeekStat (
        week=1,
        player_id=57,
        points=5,
        goals=0,
        assists=1,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw394 = GameWeekStat (
        week=2,
        player_id=57,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw395 = GameWeekStat (
        week=3,
        player_id=57,
        points=5,
        goals=0,
        assists=1,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw396 = GameWeekStat (
        week=4,
        player_id=57,
        points=6,
        goals=1,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw397 = GameWeekStat (
        week=5,
        player_id=57,
        points=8,
        goals=0,
        assists=2,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw398 = GameWeekStat (
        week=6,
        player_id=57,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw399 = GameWeekStat (
        week=7,
        player_id=57,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    # Luca Toni - 2006

    gw400 = GameWeekStat (
        week=1,
        player_id=58,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw401 = GameWeekStat (
        week=2,
        player_id=58,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw402 = GameWeekStat (
        week=3,
        player_id=58,
        points=0,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw403 = GameWeekStat (
        week=4,
        player_id=58,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw404 = GameWeekStat (
        week=5,
        player_id=58,
        points=10,
        goals=2,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw405 = GameWeekStat (
        week=6,
        player_id=58,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw406 = GameWeekStat (
        week=7,
        player_id=58,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    # Del Piero - 2006

    gw407 = GameWeekStat (
        week=1,
        player_id=59,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw408 = GameWeekStat (
        week=2,
        player_id=59,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw409 = GameWeekStat (
        week=3,
        player_id=59,
        points=0,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw410 = GameWeekStat (
        week=4,
        player_id=59,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw411 = GameWeekStat (
        week=5,
        player_id=59,
        points=0,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw412 = GameWeekStat (
        week=6,
        player_id=59,
        points=6,
        goals=1,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw413 = GameWeekStat (
        week=7,
        player_id=59,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    # Zinedine Zidane 2006 

    gw414 = GameWeekStat (
        week=1,
        player_id=60,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw415 = GameWeekStat (
        week=2,
        player_id=60,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw416 = GameWeekStat (
        week=3,
        player_id=60,
        points=0,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw417 = GameWeekStat (
        week=4,
        player_id=60,
        points=10,
        goals=1,
        assists=1,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw418 = GameWeekStat (
        week=5,
        player_id=60,
        points=12,
        goals=0,
        assists=1,
        clean_sheet=True,
        man_of_the_match=True,
    )

    gw419 = GameWeekStat (
        week=6,
        player_id=60,
        points=8,
        goals=1,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw420 = GameWeekStat (
        week=7,
        player_id=60,
        points=7,
        goals=1,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    # Marcos Brazil 2002

    gw421 = GameWeekStat (
        week=1,
        player_id=61,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw422 = GameWeekStat (
        week=2,
        player_id=61,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw423 = GameWeekStat (
        week=3,
        player_id=61,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw424 = GameWeekStat (
        week=4,
        player_id=61,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw425 = GameWeekStat (
        week=5,
        player_id=61,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw426 = GameWeekStat (
        week=6,
        player_id=61,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw427 = GameWeekStat (
        week=7,
        player_id=61,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    # Cafu 2002

    gw428 = GameWeekStat (
        week=1,
        player_id=62,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw429 = GameWeekStat (
        week=2,
        player_id=62,
        points=9,
        goals=0,
        assists=1,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw430 = GameWeekStat (
        week=3,
        player_id=62,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw431 = GameWeekStat (
        week=4,
        player_id=62,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw432 = GameWeekStat (
        week=5,
        player_id=62,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw433 = GameWeekStat (
        week=6,
        player_id=62,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw434 = GameWeekStat (
        week=7,
        player_id=62,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    # Roberto Carlos 2002

    gw435 = GameWeekStat (
        week=1,
        player_id=63,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw436 = GameWeekStat (
        week=2,
        player_id=63,
        points=18,
        goals=1,
        assists=0,
        clean_sheet=True,
        man_of_the_match=True,
    )

    gw437 = GameWeekStat (
        week=3,
        player_id=63,
        points=0,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw438 = GameWeekStat (
        week=4,
        player_id=63,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw439 = GameWeekStat (
        week=5,
        player_id=63,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw440 = GameWeekStat (
        week=6,
        player_id=63,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw441 = GameWeekStat (
        week=7,
        player_id=63,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    # Edmilson Brazil 2002

    gw442 = GameWeekStat (
        week=1,
        player_id=64,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw443 = GameWeekStat (
        week=2,
        player_id=64,
        points=0,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw444 = GameWeekStat (
        week=3,
        player_id=64,
        points=11,
        goals=1,
        assists=1,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw445 = GameWeekStat (
        week=4,
        player_id=64,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw446 = GameWeekStat (
        week=5,
        player_id=64,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw447 = GameWeekStat (
        week=6,
        player_id=64,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw448 = GameWeekStat (
        week=7,
        player_id=64,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    # Lucio 2002 WC

    gw449 = GameWeekStat (
        week=1,
        player_id=65,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw450 = GameWeekStat (
        week=2,
        player_id=65,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw451 = GameWeekStat (
        week=3,
        player_id=65,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw452 = GameWeekStat (
        week=4,
        player_id=65,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw453 = GameWeekStat (
        week=5,
        player_id=65,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw454 = GameWeekStat (
        week=6,
        player_id=65,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw455 = GameWeekStat (
        week=7,
        player_id=65,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    # Roque Junior

    gw456 = GameWeekStat (
        week=1,
        player_id=66,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw457 = GameWeekStat (
        week=2,
        player_id=66,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw458 = GameWeekStat (
        week=3,
        player_id=66,
        points=0,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw459 = GameWeekStat (
        week=4,
        player_id=66,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw460 = GameWeekStat (
        week=5,
        player_id=66,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw461 = GameWeekStat (
        week=6,
        player_id=66,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw462 = GameWeekStat (
        week=7,
        player_id=66,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    # Gilberto Silva 2002

    gw463 = GameWeekStat (
        week=1,
        player_id=67,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw464 = GameWeekStat (
        week=2,
        player_id=67,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw465 = GameWeekStat (
        week=3,
        player_id=67,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw466 = GameWeekStat (
        week=4,
        player_id=67,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw467 = GameWeekStat (
        week=5,
        player_id=67,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw468 = GameWeekStat (
        week=6,
        player_id=67,
        points=6,
        goals=0,
        assists=1,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw469 = GameWeekStat (
        week=7,
        player_id=67,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    # Juninho Paulista - 2002

    gw470 = GameWeekStat (
        week=1,
        player_id=68,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw471 = GameWeekStat (
        week=2,
        player_id=68,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw472 = GameWeekStat (
        week=3,
        player_id=68,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw473 = GameWeekStat (
        week=4,
        player_id=68,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw474 = GameWeekStat (
        week=5,
        player_id=68,
        points=0,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw475 = GameWeekStat (
        week=6,
        player_id=68,
        points=0,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw476 = GameWeekStat (
        week=7,
        player_id=68,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    # Ronaldinho 2002

    gw477 = GameWeekStat (
        week=1,
        player_id=69,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw478 = GameWeekStat (
        week=2,
        player_id=69,
        points=11,
        goals=1,
        assists=1,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw479 = GameWeekStat (
        week=3,
        player_id=69,
        points=0,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw480 = GameWeekStat (
        week=4,
        player_id=69,
        points=5,
        goals=0,
        assists=1,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw481 = GameWeekStat (
        week=5,
        player_id=69,
        points=10,
        goals=1,
        assists=1,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw482 = GameWeekStat (
        week=6,
        player_id=69,
        points=0,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw483 = GameWeekStat (
        week=7,
        player_id=69,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    # Rivaldo 02

    gw484 = GameWeekStat (
        week=1,
        player_id=70,
        points=15,
        goals=1,
        assists=1,
        clean_sheet=False,
        man_of_the_match=True,
    )

    gw485 = GameWeekStat (
        week=2,
        player_id=70,
        points=6,
        goals=1,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw486 = GameWeekStat (
        week=3,
        player_id=70,
        points=6,
        goals=1,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw487 = GameWeekStat (
        week=4,
        player_id=70,
        points=12,
        goals=1,
        assists=0,
        clean_sheet=True,
        man_of_the_match=True,
    )

    gw488 = GameWeekStat (
        week=5,
        player_id=70,
        points=12,
        goals=1,
        assists=0,
        clean_sheet=False,
        man_of_the_match=True,
    )

    gw489 = GameWeekStat (
        week=6,
        player_id=70,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw490 = GameWeekStat (
        week=7,
        player_id=70,
        points=5,
        goals=0,
        assists=1,
        clean_sheet=True,
        man_of_the_match=False,
    )

    # Miroslav Klose 2002

    gw491 = GameWeekStat (
        week=1,
        player_id=71,
        points=20,
        goals=3,
        assists=0,
        clean_sheet=True,
        man_of_the_match=True,
    )

    gw492 = GameWeekStat (
        week=2,
        player_id=71,
        points=6,
        goals=1,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw493 = GameWeekStat (
        week=3,
        player_id=71,
        points=14,
        goals=1,
        assists=1,
        clean_sheet=True,
        man_of_the_match=True,
    )

    gw494 = GameWeekStat (
        week=4,
        player_id=71,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw495 = GameWeekStat (
        week=5,
        player_id=71,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw496 = GameWeekStat (
        week=6,
        player_id=71,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw497 = GameWeekStat (
        week=7,
        player_id=71,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    # Miroslav Klose 2006

    gw498 = GameWeekStat (
        week=1,
        player_id=72,
        points=16,
        goals=2,
        assists=0,
        clean_sheet=False,
        man_of_the_match=True,
    )

    gw499 = GameWeekStat (
        week=2,
        player_id=72,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw500 = GameWeekStat (
        week=3,
        player_id=72,
        points=16,
        goals=2,
        assists=0,
        clean_sheet=True,
        man_of_the_match=True,
    )

    gw501 = GameWeekStat (
        week=4,
        player_id=72,
        points=8,
        goals=0,
        assists=2,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw502 = GameWeekStat (
        week=5,
        player_id=72,
        points=6,
        goals=1,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw503 = GameWeekStat (
        week=6,
        player_id=72,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw504 = GameWeekStat (
        week=7,
        player_id=72,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    # Michael Ballack 2006

    gw505 = GameWeekStat (
        week=1,
        player_id=73,
        points=14,
        goals=1,
        assists=2,
        clean_sheet=True,
        man_of_the_match=True,
    )

    gw506 = GameWeekStat (
        week=2,
        player_id=73,
        points=5,
        goals=0,
        assists=1,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw507 = GameWeekStat (
        week=3,
        player_id=73,
        points=6,
        goals=0,
        assists=1,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw508 = GameWeekStat (
        week=4,
        player_id=73,
        points=3,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw509 = GameWeekStat (
        week=5,
        player_id=73,
        points=8,
        goals=1,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw510 = GameWeekStat (
        week=6,
        player_id=73,
        points=14,
        goals=1,
        assists=0,
        clean_sheet=True,
        man_of_the_match=True,
    )

    gw511 = GameWeekStat (
        week=7,
        player_id=73,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    # Oliver Kahn 2002

    gw512 = GameWeekStat (
        week=1,
        player_id=74,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw513 = GameWeekStat (
        week=2,
        player_id=74,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw514 = GameWeekStat (
        week=3,
        player_id=74,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw515 = GameWeekStat (
        week=4,
        player_id=74,
        points=12,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=True,
    )

    gw516 = GameWeekStat (
        week=5,
        player_id=74,
        points=12,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=True,
    )

    gw517 = GameWeekStat (
        week=6,
        player_id=74,
        points=6,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw518 = GameWeekStat (
        week=7,
        player_id=74,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    # Kylian Mbappe 2022

    gw519 = GameWeekStat (
        week=1,
        player_id=75,
        points=15,
        goals=1,
        assists=1,
        clean_sheet=False,
        man_of_the_match=True,
    )

    gw520 = GameWeekStat (
        week=2,
        player_id=75,
        points=16,
        goals=2,
        assists=0,
        clean_sheet=False,
        man_of_the_match=True,
    )

    gw521 = GameWeekStat (
        week=3,
        player_id=75,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw522 = GameWeekStat (
        week=4,
        player_id=75,
        points=19,
        goals=2,
        assists=1,
        clean_sheet=False,
        man_of_the_match=True,
    )

    gw523 = GameWeekStat (
        week=5,
        player_id=75,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw524 = GameWeekStat (
        week=6,
        player_id=75,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw525 = GameWeekStat (
        week=7,
        player_id=75,
        points=14,
        goals=3,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    # Harry Kane 2018

    gw526 = GameWeekStat (
        week=1,
        player_id=76,
        points=16,
        goals=2,
        assists=0,
        clean_sheet=False,
        man_of_the_match=True,
    )

    gw527 = GameWeekStat (
        week=2,
        player_id=76,
        points=20,
        goals=3,
        assists=0,
        clean_sheet=False,
        man_of_the_match=True,
    )

    gw528 = GameWeekStat (
        week=3,
        player_id=76,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw529 = GameWeekStat (
        week=4,
        player_id=76,
        points=12,
        goals=1,
        assists=0,
        clean_sheet=False,
        man_of_the_match=True,
    )

    gw530 = GameWeekStat (
        week=5,
        player_id=76,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw531 = GameWeekStat (
        week=6,
        player_id=76,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw532 = GameWeekStat (
        week=7,
        player_id=76,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )


    # Luka Modric 2018

    gw533 = GameWeekStat (
        week=1,
        player_id=77,
        points=14,
        goals=1,
        assists=0,
        clean_sheet=True,
        man_of_the_match=True,
    )

    gw534 = GameWeekStat (
        week=2,
        player_id=77,
        points=14,
        goals=1,
        assists=0,
        clean_sheet=True,
        man_of_the_match=True,
    )

    gw535 = GameWeekStat (
        week=3,
        player_id=77,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw536 = GameWeekStat (
        week=4,
        player_id=77,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw537 = GameWeekStat (
        week=5,
        player_id=77,
        points=11,
        goals=0,
        assists=1,
        clean_sheet=False,
        man_of_the_match=True,
    )

    gw538 = GameWeekStat (
        week=6,
        player_id=77,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw539 = GameWeekStat (
        week=7,
        player_id=77,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )


    # Lionel Messi 2014

    gw540 = GameWeekStat (
        week=1,
        player_id=78,
        points=12,
        goals=1,
        assists=0,
        clean_sheet=False,
        man_of_the_match=True,
    )

    gw541 = GameWeekStat (
        week=2,
        player_id=78,
        points=12,
        goals=1,
        assists=0,
        clean_sheet=True,
        man_of_the_match=True,
    )

    gw542 = GameWeekStat (
        week=3,
        player_id=78,
        points=16,
        goals=2,
        assists=0,
        clean_sheet=False,
        man_of_the_match=True,
    )

    gw543 = GameWeekStat (
        week=4,
        player_id=78,
        points=11,
        goals=0,
        assists=1,
        clean_sheet=True,
        man_of_the_match=True,
    )

    gw544 = GameWeekStat (
        week=5,
        player_id=78,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw545 = GameWeekStat (
        week=6,
        player_id=78,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw546 = GameWeekStat (
        week=7,
        player_id=78,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    # Thomas Muller 2010

    gw547 = GameWeekStat (
        week=1,
        player_id=79,
        points=9,
        goals=1,
        assists=1,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw548 = GameWeekStat (
        week=2,
        player_id=79,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw549 = GameWeekStat (
        week=3,
        player_id=79,
        points=5,
        goals=0,
        assists=1,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw550 = GameWeekStat (
        week=4,
        player_id=79,
        points=19,
        goals=2,
        assists=1,
        clean_sheet=False,
        man_of_the_match=True,
    )

    gw551 = GameWeekStat (
        week=5,
        player_id=79,
        points=6,
        goals=1,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw552 = GameWeekStat (
        week=6,
        player_id=79,
        points=0,
        goals=0,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw553 = GameWeekStat (
        week=7,
        player_id=79,
        points=12,
        goals=1,
        assists=0,
        clean_sheet=False,
        man_of_the_match=True,
    )


    # Diego Forlan 2010

    gw554 = GameWeekStat (
        week=1,
        player_id=80,
        points=8,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=True,
    )

    gw555 = GameWeekStat (
        week=2,
        player_id=80,
        points=16,
        goals=2,
        assists=0,
        clean_sheet=False,
        man_of_the_match=True,
    )

    gw556 = GameWeekStat (
        week=3,
        player_id=80,
        points=2,
        goals=0,
        assists=0,
        clean_sheet=True,
        man_of_the_match=False,
    )

    gw557 = GameWeekStat (
        week=4,
        player_id=80,
        points=5,
        goals=0,
        assists=1,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw558 = GameWeekStat (
        week=5,
        player_id=80,
        points=12,
        goals=1,
        assists=0,
        clean_sheet=False,
        man_of_the_match=True,
    )

    gw559 = GameWeekStat (
        week=6,
        player_id=80,
        points=6,
        goals=1,
        assists=0,
        clean_sheet=False,
        man_of_the_match=False,
    )

    gw560 = GameWeekStat (
        week=7,
        player_id=80,
        points=6,
        goals=1,
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
            gw112,
            gw113,
            gw114,
            gw115,
            gw116,
            gw117,
            gw118,
            gw119,
            gw120,
            gw121,
            gw122,
            gw123,
            gw124,
            gw125,
            gw126,
            gw127,
            gw128,
            gw129,
            gw130,
            gw131,
            gw132,
            gw133,
            gw134,
            gw135,
            gw136,
            gw137,
            gw138,
            gw139,
            gw140,
            gw141,
            gw142,
            gw143,
            gw144,
            gw145,
            gw146,
            gw147,
            gw148,
            gw149,
            gw150,
            gw151,
            gw152,
            gw153,
            gw154,
            gw155,
            gw156,
            gw157,
            gw158,
            gw159,
            gw160,
            gw161,
            gw162,
            gw163,
            gw164,
            gw165,
            gw166,
            gw167,
            gw168,
            gw169,
            gw170,
            gw171,
            gw172,
            gw173,
            gw174,
            gw175,
            gw176,
            gw177,
            gw178,
            gw179,
            gw180,
            gw181,
            gw182,
            gw183,
            gw184,
            gw185,
            gw186,
            gw187,
            gw188,
            gw189,
            gw190,
            gw191,
            gw192,
            gw193,
            gw194,
            gw195,
            gw196,
            gw197,
            gw198,
            gw199,
            gw200,
            gw201,
            gw202,
            gw203,
            gw204,
            gw205,
            gw206,
            gw207,
            gw208,
            gw209,
            gw210,
            gw211,
            gw212,
            gw213,
            gw214,
            gw215,
            gw216,
            gw217,
            gw218,
            gw219,
            gw220,
            gw221,
            gw222,
            gw223,
            gw224,
            gw225,
            gw226,
            gw227,
            gw228,
            gw229,
            gw230,
            gw231,
            gw232,
            gw233,
            gw234,
            gw235,
            gw236,
            gw237,
            gw238,
            gw239,
            gw240,
            gw241,
            gw242,
            gw243,
            gw244,
            gw245,
            gw246,
            gw247,
            gw248,
            gw249,
            gw250,
            gw251,
            gw252,
            gw253,
            gw254,
            gw255,
            gw256,
            gw257,
            gw258,
            gw259,
            gw260,
            gw261,
            gw262,
            gw263,
            gw264,
            gw265,
            gw266,
            gw267,
            gw268,
            gw269,
            gw270,
            gw271,
            gw272,
            gw273,
            gw274,
            gw275,
            gw276,
            gw277,
            gw278,
            gw279,
            gw280,
            gw281,
            gw282,
            gw283,
            gw284,
            gw285,
            gw286,
            gw287,
            gw288,
            gw289,
            gw290,
            gw291,
            gw292,
            gw293,
            gw294,
            gw295,
            gw296,
            gw297,
            gw298,
            gw299,
            gw300,
            gw301,
            gw302,
            gw303,
            gw304,
            gw305,
            gw306,
            gw307,
            gw308,
            gw309,
            gw310,
            gw311,
            gw312,
            gw313,
            gw314,
            gw315,
            gw316,
            gw317,
            gw318,
            gw319,
            gw320,
            gw321,
            gw322,
            gw323,
            gw324,
            gw325,
            gw326,
            gw327,
            gw328,
            gw329,
            gw330,
            gw331,
            gw332,
            gw333,
            gw334,
            gw335,
            gw336,
            gw337,
            gw338,
            gw339,
            gw340,
            gw341,
            gw342,
            gw343,
            gw344,
            gw345,
            gw346,
            gw347,
            gw348,
            gw349,
            gw350,
            gw351,
            gw352,
            gw353,
            gw354,
            gw355,
            gw356,
            gw357,
            gw358,
            gw359,
            gw360,
            gw361,
            gw362,
            gw363,
            gw364,
            gw365,
            gw366,
            gw367,
            gw368,
            gw369,
            gw370,
            gw371,
            gw372,
            gw373,
            gw374,
            gw375,
            gw376,
            gw377,
            gw378,
            gw379,
            gw380,
            gw381,
            gw382,
            gw383,
            gw384,
            gw385,
            gw386,
            gw387,
            gw388,
            gw389,
            gw390,
            gw391,
            gw392,
            gw393,
            gw394,
            gw395,
            gw396,
            gw397,
            gw398,
            gw399,
            gw400,
            gw401,
            gw402,
            gw403,
            gw404,
            gw405,
            gw406,
            gw407,
            gw408,
            gw409,
            gw410,
            gw411,
            gw412,
            gw413,
            gw414,
            gw415,
            gw416,
            gw417,
            gw418,
            gw419,
            gw420,
            gw421,
            gw422,
            gw423,
            gw424,
            gw425,
            gw426,
            gw427,
            gw428,
            gw429,
            gw430,
            gw431,
            gw432,
            gw433,
            gw434,
            gw435,
            gw436,
            gw437,
            gw438,
            gw439,
            gw440,
            gw441,
            gw442,
            gw443,
            gw444,
            gw445,
            gw446,
            gw447,
            gw448,
            gw449,
            gw450,
            gw451,
            gw452,
            gw453,
            gw454,
            gw455,
            gw456,
            gw457,
            gw458,
            gw459,
            gw460,
            gw461,
            gw462,
            gw463,
            gw464,
            gw465,
            gw466,
            gw467,
            gw468,
            gw469,
            gw470,
            gw471,
            gw472,
            gw473,
            gw474,
            gw475,
            gw476,
            gw477,
            gw478,
            gw479,
            gw480,
            gw481,
            gw482,
            gw483,
            gw484,
            gw485,
            gw486,
            gw487,
            gw488,
            gw489,
            gw490,
            gw491,
            gw492,
            gw493,
            gw494,
            gw495,
            gw496,
            gw497,
            gw498,
            gw499,
            gw500,
            gw501,
            gw502,
            gw503,
            gw504,
            gw505,
            gw506,
            gw507,
            gw508,
            gw509,
            gw510,
            gw511,
            gw512,
            gw513,
            gw514,
            gw515,
            gw516,
            gw517,
            gw518,
            gw519,
            gw520,
            gw521,
            gw522,
            gw523,
            gw524,
            gw525,
            gw526,
            gw527,
            gw528,
            gw529,
            gw530,
            gw531,
            gw532,
            gw533,
            gw534,
            gw535,
            gw536,
            gw537,
            gw538,
            gw539,
            gw540,
            gw541,
            gw542,
            gw543,
            gw544,
            gw545,
            gw546,
            gw547,
            gw548,
            gw549,
            gw550,
            gw551,
            gw552,
            gw553,
            gw554,
            gw555,
            gw556,
            gw557,
            gw558,
            gw559,
            gw560,
        ]
    )
    db.session.commit()


def undo_game_week_stats():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.game_week_stat RESTART IDENTITY CASCADE;"
        )
    else:
        db.session.execute("DELETE FROM game_week_stat")

    db.session.commit()
