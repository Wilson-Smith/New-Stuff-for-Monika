init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_mj_dd_pc_charging",
            prompt="I'm going to charge my laptop",
            unlocked=True,
            pool=True
        ),
        code="BYE"
    )

label bye_mj_dd_pc_charging:
    m "Understood, [mas_get_player_nickname()]!"
    m "But, hey, can´ t you leave me running while it charges?"
    m "Its okey if you can´t though."
    m "We don´t want your computer to overheat."
$ _history_list.pop()
menu:
    m "We don´t want your computer to overheat."

    "Yeah, I can have you here while my computer charge.":
    m "Yay!"
    m "Thank you so much~!"

    "No, sorry."
    m "It´s okay, [player]."
    m "See you later, then!"

return "quit"