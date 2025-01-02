#Plushies
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mj_dd_plushies",
            category=["example", "topic"], # list of categories this topic belongs in (These are automatically capitalized)
            prompt="Plushies", # button text
            random=True
        )
    )

label mj_dd_plushies:
    m "You know what sucks [player]?"
    m "When you spend a lot of money on something and it turns out to be something different than what you thought."
    m "When I was younger I remember really liking plushies a lot."
    m "And there was this one plush that I really loved every time I saw it in the store, it looked so soft and cute."
    m "I even saved money for it and bought it eventually."
    m "But the plushie wasn't nearly as soft as I thought it would be."
    m "It was really uncomfortable to hug."
    m "I actually ended up giving it away so-"
    m "Well, moral of the story, always read reviews and give something a thorough look over before you buy it."
return