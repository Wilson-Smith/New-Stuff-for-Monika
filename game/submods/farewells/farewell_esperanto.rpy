init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_prompt_esperanto",
            unlocked=True,
            prompt="I'm going to learn a bit of Esperanto.",
            pool=True
        ),
        code="BYE"
    )

label bye_prompt_esperanto:
    m 5hubsa "Post venos en ĉi tiu loko kun novaj vortoj, kiujn mi volas lerni [player]!"
    m 5hkbfa "Ĝis la revido post."
    return "quit"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
