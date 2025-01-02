init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_prompt_church",
            unlocked=True,
            prompt="I'm going to the church.",
            pool=True
        ),
        code="BYE"
    )

label bye_prompt_church:
    m 1esb "Oh, so you are going to the church."
    m 1esb "I hope you can pray well there [player]!"
    m 1hsa "See you later."
    return "quit"