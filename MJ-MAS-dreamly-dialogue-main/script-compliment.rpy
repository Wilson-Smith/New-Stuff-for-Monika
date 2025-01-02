init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="mj_dd_soulmate",
            prompt="You are my soulmate!",
            unlocked=True
        ),
        code="CMP"
    )

label mj_dd_soulmate: #TODO
    "You are my Soulmate!"
    m "y-you're soulmate?"
    m "That's so sweet..."
    m "It truly does feel like we were destined for each other you know~"
    m "[player] you're always saying the most romantic things to me."
    m "You're my soulmate as well!"