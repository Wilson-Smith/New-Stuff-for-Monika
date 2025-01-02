init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_mj_dd_pc_burning",
            prompt="My PC is burning up.",
            unlocked=True,
            pool=True
        ),
        code="BYE"
    )

label bye_mj_dd_pc_burning:
    m 1wud "Oh!"
    m 3ekb "Understood, [player]!"
    m 2eksdlc "Please, take care of your computer."
    m 2hua "See you later~."
return "quit"