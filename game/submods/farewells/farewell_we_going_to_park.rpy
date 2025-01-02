init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_going_to_the_park",
            unlocked=True,
            prompt="We're going to the park.",
            pool=True
        ),
        code="BYE"
    )

label bye_going_to_the_park:
    m 1hub "Very nice choise [player]!"
    m 1hua "I like it!"
    jump bye_going_somewhere_post_aff_check

label bye_going_somewhere_post_aff_check:
    # il file creato proviene da mas_dockstat_iostart, quindi è questo il generativo di Moni
    jump mas_dockstat_iostart
