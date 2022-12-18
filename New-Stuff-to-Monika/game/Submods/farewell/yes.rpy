init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="byebye", # event label (MUST BE UNIQUE)
            category=["."], # list of categories this topic belongs in (These are automatically capitalized)
            prompt="bye", # button text
            random=True, # True if this topic should appear randomly
            pool=True # True if this topic should appear in "Ask a Question"
        )
    )

label byebye:
    m 1esa "."
    return "quit"