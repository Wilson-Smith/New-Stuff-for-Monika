
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_example", # event label (MUST BE UNIQUE)
            category=["example", "topic"], # list of categories this topic belongs in (These are automatically capitalized)
            prompt="Example Topic", # button text
            random=True, # True if this topic should appear randomly
            pool=True # True if this topic should appear in "Ask a Question"
        )
    )

label monika_example:
    m 1esa "This is an example topic."
    m 1sub "I feel like this doesn't actually belong here..."
    m 6ltp "Why would somebody just add the example template directly into the mod?"
    m 5ruu "They really shouldn't be allowed to contribute to this repository anymore."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_example_based", # event label (MUST BE UNIQUE)
            category=["example", "topic"], # list of categories this topic belongs in (These are automatically capitalized)
            prompt="Example Topic Based", # button text
            random=True, # True if this topic should appear randomly
            pool=True # True if this topic should appear in "Ask a Question"
        )
    )

label monika_example_based:
    m 1a "."
    m 3d ".."
    m 2e "..."
    m 5r "...."
    return
