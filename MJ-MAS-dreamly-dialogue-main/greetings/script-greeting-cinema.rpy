init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="mj_dd_greeting_cinema",
            unlocked=True,
            category=[store.mas_greetings.TYPE_MJ_DD_CINEMA],
        ),
        code="GRE"
    )

label mj_dd_greeting_cinema:
    if mas_getAbsenceLength() >= datetime.timedelta(hours=6):
        m "Oh-[w=0.4]{nw}"
        extend " Welcome back, [player]!"
        m "Gosh, you were gone for a while, ahaha!"
        m "Did you end up watching more than one movie?"
        extend " Or maybe you went out somewhere else afterwards?"
        m "Either way I hope you had fun today."
        m "And if not, hopefully spending some time with your lovely girlfriend will help boost your mood back up!"
        jump mm_dd_greeting_cinema_moviechoice
    elif mas_getAbsenceLength() >= datetime.timedelta(hours=2) and mas_getAbsenceLength() <= datetime.timedelta(hours=6):
        m 1eub "Welcome back, [player]!"
        m 1hub "I hope you had a wonderful time at the cinema!"
        jump mm_dd_greeting_cinema_moviechoice
    else:
        m "Oh-[w=0.4]{nw}"
        extend " Hello again [player]!"
        m "Sorry, you surprised me a little."
        m "I thought you'd be out for longer."
        m "Did something happen?{nw}"
        menu:
            m "Did something happen?{fast}"
            "It was just a short film.":
                m "Oh!"
                m "Oh good, I thought something might've made you unable to go."
                m "Glad to know that wasn't the case, ahaha!"
                jump mm_dd_greeting_cinema_moviechoice
            "I had to leave early.":
                m "Aw, I'm so sorry to hear that [player]."
                m "I hope it wasn't something too serious that made you have to leave."
                m "Maybe we can find the movie you went to see online, if you want?"
                m "At least then you won't be left on a cliffhanger, ahaha."
                jump mj_dd_greeting_cinemaend
            "I couldn't go.":
                m "Aw, I'm so sorry to hear that [player]."
                m "I hope it wasn't something too serious that made you stay here."
                m "There's always another day to go, though!"
                m "Maybe we can find the movie you wanted see online, if you want?"
                m "We can make it a whole movie night then at, ahaha!"
                jump mj_dd_greeting_cinemaend

label mm_dd_greeting_cinema_moviechoice:
    $ ev = mas_getEV("monika_horror")
    m 3wud "What kind of movie did you go see, by the way?{nw}"
    $ _history_list.pop()
    menu:
        m "What kind of movie did you go see, by the way?{fast}"
        "An horror movie.":
            m 2wud "Ooh!"
            if ev.shown_count == 0:
                m 2rua "I remember how we discussed the hardship of creating an horror movie nowadays."

            m "Elaborating an actual scary movie takes a lot nowadays."
            m "It's necessary that it isn't plagiated of cheap jumpscares and stereotypical tropes."
            m "Anyway! As scary as that movie could be, there is nothing to fear now."
            m "You're here, you're safe. I will take care of you, okay?" # (if high aff maybe putting a "<3" as well)

        "Comedy/Romance":
            m "Going for something lighter, player?"
            m "Ahaha!"
            m "You need to be careful while writing comedy or romance, though."
            m "It is so easy to fall into the cinematic rabbit hole of cliches."
            m "Buuut... at the same time..."
            m "I dream of a day where we can both go to the cinema together~"
            m "And maybe... watch a romantic movie by your side..."
            m "Wouldn't that be perfect, player?"
            m "But then again, this reality is our personal movie for now. I love you!"

        "thriller/mystery":
            m "Interesting choice, indeed!"
            m "You see, mystery can be one of my go-to choices in terms of picking movies."
            m "If well done, they can grasp your attention since the very beginning..."
            m "...and the mysteries can be so well fabricated they may submerge you into the plot all the way!"
            m "I hope watching that movie was a great experience. Now we can hang out for a little bit. Hehehe~"

        "cartoon movie/anime":
            m "A cartoon movie! That's sweet!"
            m "You know, I would not mind at all if you wanted to take me to watch some animated media when I cross over."
            m "I might not be accustomed to it, but, if it's for you, I will definitely give it a try!"
            m "Come to think of it, maybe Natsuki would be the type to enjoy that kind of stuff, wouldn't she?"
            m "Anyway! Ready to spend some more time together, player~?""

label mj_dd_greeting_cinemaend:
    return