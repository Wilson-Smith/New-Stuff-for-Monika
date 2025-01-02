init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_mj_dd_thundering",
            prompt="It´s thundering.",
            unlocked=True,
            pool=True
        ),
        code="BYE"
    )

label bye_mj_dd_thundering:
    m 1ekc "Oh..."
    m 1eka "Thanks for letting me know, [player]!"
    m 2ekc "Please, be safe..."
    m 2ekc "...and if you happen to need to get out of your home, try to avoid lighting as much as you can."
    m 3eka "I love you so much. Come back safe to me!"
return "quit"