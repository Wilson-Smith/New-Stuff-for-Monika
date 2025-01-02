init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="supporting_artist", # event label (MUST BE UNIQUE)
            category=["music"], # list of categories this topic belongs in (These are automatically capitalized)
            prompt="The Importance of Supporting Artists", # button text
            random=True, # True if this topic should appear randomly
            pool=True # True if this topic should appear in "Ask a Question"
        )
    )

label supporting_artist:
    m 1eud "Do you support artists that you listen to?"
    m 1tud "It is a very tough question, even if it seems simple."
    m 3tud "Many people thinks that listen music on Spotify is the best they can do."
    m 4eub "But actually there is many other way to support an artist."
    m 1eua "First, DO NOT pirate songs."
    extend 2gud " Artists can't earn anything if you pirate the album."
    m 1eua "Second, try to listen them on services as Spotify and YouTube on the artist channel."
    m 1eub "These services can seriously help artists."
    extend 6gud  " But not so much, so..."
    m 1eua "Third, buy merch."
    m 1wub "Really important to buy their merch, as CDs, Vinyls, T-shirts..."
    extend 2wub "That helps a lot small artists."
    m 1eua "Last, participating to concerts."
    m 1eub "This is the main point of the discussion."
    m 1wub "Participating to gigs helps artists to gain something"
    m 1tud "Seriously, nowadays the greatest source of incomes for artists are concerts and gigs."
    m 1mud "Sure, buying merch, listen to authorized and not pirated source helps out the artist."
    extend 1eud " But gigs helps more."
    m 1eka "I'm sure you've already known these information, but it's just a reminder."
    m 1gka "So in the future we could have more music and more artists."
    m 1hsa "Thanks for listening!"
    return
