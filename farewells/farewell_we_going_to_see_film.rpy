init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_we_going_to_see_film",
            unlocked=True,
            prompt="We're going to see a film",
            pool=True
        ),
        code="BYE"
    )

label bye_we_going_to_see_film:
    m 1wua "Interesting!"
    extend 1wub "What genre is it?"
    $ _history_list.pop()
    menu:
        "Action":
            m 1wub "That's nice!"
            extend 2euc "I wonder what type of action will be."
            m 5eub "But sure-fire it will be great."
        "Crime":
            m 1eub "That's curious"
            extend 2euc "I wonder what will happen."
        "Drama":
            m 1eua "Oh, nice choise!"
        "Fantasy":
            m 1eub "I've read 'Lord of Rings', it was beautiful."
            m 1eua "I hope it will be at the same level!"
        "Horror":
            m 6csa "..."
            m 6csa "..."
            m 6csa "..."
            m 6csa "[player]..."
            m 6csb "DO NOT BE AFRAID..."
            extend 6csb "I'M INSIDE YOUR WALLS"
            m 1tkb "Have I scared you, [player]?"
            m 1eub "Anyway..."
        "Comedy":
            m 1eua "'The best cure is the laught'"
            extend 1nua "I hope you like laught a lot, [player]"
            m 1hua "hehe~"
        "Romance":
            m 1tku "Ooh!"
            extend 1tkb "It will be like our story, isn't it?"
            $ _history_list.pop()
            menu:
                "Yes":
                    m 1fkbfb "Oh [player]..."           
        "Science Fiction":
            m 1sut "Sci-fi is my favourite genre."
            m 1wub "Now I'm really interested."
        "Sports":
            m 1eub "That's kinda curious!"
        "Thriller":
            m 1euc "But we are going to see a movie, or"
            extend 3kub "we are going to listen to Michael Jackson?"
            m 1eua "However..."
        "Mystery":
            m 1mfp "Now I have to see an entire film for the answer!"
            extend 1mft "Can you spoil it now?"
            m 3wft "Why do I have to see an entire film for a simple mystery"
            m 1tuu "I hope you notice the irony,"
            extend 1eub "and I really like it."
            m 1eua "Anyway..."
        "War":
            m 1eub "Really interestig choise!"
        "Western":
            m 1eub "Uh"
            extend 6efu "Then we'll do a duel, officer."
            m 4efu "It will be law against outlaw."
            m 1eub "However..."

        "It isn't on the list":
            m 1eub "Surely it's a good movie."
    jump bye_going_somewhere_post_aff_check

label bye_going_somewhere_post_aff_check:
    # il file creato proviene da mas_dockstat_iostart, quindi è questo il generativo di Moni
    jump mas_dockstat_iostart
