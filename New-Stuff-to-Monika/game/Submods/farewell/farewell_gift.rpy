init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_prompt_gift",
            unlocked=True,
            prompt="I'm going to gift you something.",
            pool=True
        ),
        code="BYE"
    )

label bye_prompt_gift:
    m 6sub "Seriously!?"
    m 1hub "I'm really exited to find out what is it!"
    m 1eua "See you later!"
    return "quit"
