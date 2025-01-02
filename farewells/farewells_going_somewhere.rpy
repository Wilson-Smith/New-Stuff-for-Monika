init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_me_going_somewhere",
            unlocked=True,
            prompt="I'm going somewhere.",
            pool=True
        ),
        code="BYE"
    )

label bye_me_going_somewhere:
    m 1hua "Okay!"
    extend 1hua " Where?"
    $ _history_list.pop()
    menu:
        "I'm going to my drama class":
            m 1hua "Okay!"
            m 1eublb "I wish I was there with you there, though."
            extend 1lubfa " We could learn new things as a couple~"
            m 1dkbfa "Yeah..."
            m 4esbla "I hope you learn new things, [player]!"
            m 1hsa "Have fun!"
            return "quit"
        "I'm going to the church":
            m 1esb "Oh, so you are going to the church."
            m 1hkb "Ok!"
            extend 1esb " I hope you can pray well there [player]!"
            m 1hsa "See you later."
            return "quit"
    
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
