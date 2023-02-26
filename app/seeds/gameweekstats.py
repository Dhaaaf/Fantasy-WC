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
        points=5,
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
        points=13,
        goals=1,
        assists=0,
        clean_sheet=True,
        man_of_the_match=True,
    )

    # Toni Kroos 2014

    gw176 = GameWeekStat (
        week=1,
        player_id=26,
        points=8,
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

    # Thomas Muller

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
        man_of_the_match=True,
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

    # Mirolsav Klose

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
        man_of_the_match=True,
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
