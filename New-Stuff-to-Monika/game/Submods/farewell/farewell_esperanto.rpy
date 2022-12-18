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
    m 1hua "Vere?"
    m 5ekblb "Mi volas lerni Esperanto kun vi, sed ni havas de laboras..."
    m 5hubsa "Post venos en ĉi tiu loko kun novaj vortoj, kiujn mi volas lerni [player]!"
    m 5hkbfa "Gxis la revido post."
    return "quit"
    