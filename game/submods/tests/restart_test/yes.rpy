init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="byerestart", # event label (MUST BE UNIQUE)
            category=["-"], # list of categories this topic belongs in (These are automatically capitalized)
            prompt="restartbye", # button text
            random=False, # True if this topic should appear randomly
            pool=True # True if this topic should appear in "Ask a Question"
        )
    )

label byerestart:
    jump bye_prompt_restart