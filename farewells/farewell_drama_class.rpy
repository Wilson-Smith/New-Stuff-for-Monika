init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_prompt_drama_class",
            unlocked=True,
            prompt="I'm going to my drama class.",
            pool=True
        ),
        code="BYE"
    )

label bye_prompt_drama_class:
    m 1hua "Okay!"
    m 1eublb "I wish I was there with you there, though."
    extend 1lubfa " We could learn new things as a couple~"
    m 1dkbfa "Yeah..."
    m 1hsa "Have fun!"
    return "quit"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
