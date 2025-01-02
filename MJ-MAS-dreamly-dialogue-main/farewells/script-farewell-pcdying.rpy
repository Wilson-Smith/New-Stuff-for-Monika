init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_mj_dd_pc_dying",
            prompt="My PC is dying.",
            unlocked=True,
            pool=True
        ),
        code="BYE"
    )

label bye_mj_dd_pc_dying:
    m 1dsc "Thats worrying to hear, [player]."
    m 1eka "Thank you for letting me know, though!"
    m 1ekbla "Make sure to come back to me as soon as you can!"
    m 1hub "I love you!"
return "quit"