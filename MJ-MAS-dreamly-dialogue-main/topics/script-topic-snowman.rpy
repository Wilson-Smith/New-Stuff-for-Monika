#Snowman
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mj_dd_snowman",
            category=["example", "topic"], # list of categories this topic belongs in (These are automatically capitalized)
            prompt="Snowman", # button text
            random=True
        )
    )

label mj_dd_snowman:
    m "Hey [player], have you ever made a snowman before?"
    m "Ahaha! I know it probably sounds a little childish, but playing in the snow has always been one of my favorite winter past times!"
    m "Making Snow Angels, Snowmen, and even Snowball fights!"
    m "You know [player], I'm pretty good at snowball fights!"
    m "So be sure to bring your A-game, when it comes to any future snow battles with eachother~"
    m "Ahaha!"
return