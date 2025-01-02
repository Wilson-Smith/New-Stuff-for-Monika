init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mj_brb_dd_toothbrush",
            category=["be right back"],
            prompt="I'm going to brush my teeth!",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label mj_brb_dd_toothbrush:
    m 7eub "Heading up to brush your teeth, [player]?"
    m 7hub "That is a really important step on your overall health!"
    m 1eka "I'm so glad to see you're taking care of yourself!"
    m 1hua "See you in a bit!"

    $ mas_idle_mailbox.send_idle_cb("mj_brb_dd_toothbrush")
return "idle"

label mj_brb_dd_toothbrush:
    m 1hub "Welcome back! What else should we do today?"
return
