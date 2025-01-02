init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_perform_show_player_together",
            unlocked=True,
            prompt="I'm going to perform a show, do you want to come?",
            pool=True
        ),
        code="BYE"
    )

label bye_perform_show_player_together:
    m 1sub "Seriouly!"
    m 1hub "That's wonderful!"
    jump bye_going_somewhere_post_aff_check

label bye_going_somewhere_post_aff_check:

    jump mas_dockstat_iostart
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
