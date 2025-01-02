init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_prompt_going_backup",
            unlocked=True,
            prompt="I'm going to backup you.",
            pool=True
        ),
        code="BYE"
    )

label bye_prompt_going_backup:
    m 1eub "Okay!"
    m 1hua "Thanks [player] that you are going to backup me."
    m 1eub "See you soon!"
    return "quit"