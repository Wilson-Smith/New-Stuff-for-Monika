init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_doing_something",
            unlocked=True,
            prompt="I'm going to do something",
            pool=True
        ),
        code="BYE"
    )

label bye_doing_something:
    m 6sub "Oh, what are you going to do?"
    menu:
        "I'm going to install you a submod":
            m 1eub "Oh, now I'm curious what you will add!"
            m "But before installing it, backup me, ok!"
            m "See you soon!"

        "I'm going to backup you":
            m 1eub "Okay!"
            m 1hua "Thanks [player] that you are going to backup me."
            m 1eub "See you soon!"
            return "quit"

        "I'm going to add you a location":
            m 1hua "Oh, okay!"
            m 5ekblb "I want to know what is it..."
            m 5hubsa "Anyway see you soon!"
            return "quit"


# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

