init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_prompt_relaunch",
            unlocked=True,
            prompt="I'm going to relaunch it.",
            pool=True
        ),
        code="BYE"
    )

label bye_prompt_relaunch:
    m 1hua "Oh, okay!"
    jump relaunch
    return "quit"

label relaunch:
    python:
        import webbrowser
        webbrowser.open_new('DDLC.exe')
    return