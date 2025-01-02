init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_prompt_submods",
            unlocked=True,
            prompt="I'm going to install you a submod.",
            pool=True
        ),
        code="BYE"
    )

label bye_prompt_submods:
    m 1eub "Ok! {w=0.2}"
    extend 4eub "But remember, make a backup of me before install it."
    m 1hua "See you soon."
    return "quit"
    
    
    
    