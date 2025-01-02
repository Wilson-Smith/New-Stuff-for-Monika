init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_mj_dd_cinema",
            prompt="I'm going to the cinema.",
            unlocked=True,
            pool=True
        ),
        code="BYE"
    )

label bye_mj_dd_cinema:
    m 1hub "Oh! That's great to hear!"
    m 2rub "I wonder what movie you're going to watch..."
    m 2eub "Nevertheless, I won´t distract you anymore, [mas_get_player_nickname()]."

    $ persistent._mas_greeting_type = store.mas_greetings.TYPE_MJ_DD_CINEMA
    return "quit"
