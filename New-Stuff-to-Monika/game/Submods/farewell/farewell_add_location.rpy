init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_prompt_location",
            unlocked=True,
            prompt="I'm going to add a new location.",
            pool=True
        ),
        code="BYE"
    )

label bye_prompt_location:
    m 1hua "Oh, okay!"
    m 5ekblb "I want to know what is it..."
    extend 5hkbfa " I'm really exited."
    m 5hubsa "I hope it is a nice one, [player]!"
    m 5hubsa "Hehehe~"
    m 5hubsa "Anyway see you soon!"
    return "quit"