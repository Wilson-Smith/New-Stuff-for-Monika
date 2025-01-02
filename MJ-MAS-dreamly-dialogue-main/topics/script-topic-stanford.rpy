init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mj_dd_stanfordprisonexperiment",
            category=["example", "topic"], # list of categories this topic belongs in (These are automatically capitalized)
            prompt="Stanford Prison Experiment", # button text
            random=True
        )
    )

label mj_dd_stanfordprisonexperiment:
    $ ev = mas_getEV("mj_dd_stanfordprisonexperiment")

    if ev.shown_count == 0:
        m "[player], can I talk with you about a bit of a sensitive topic?"
        m "It's about something called the Stanford Prison Experiment, if you've heard of it."
        m "If you're not okay with a darker topic like that though, that's fine, I'll keep it to myself."

    else:
        m "[player], can I talk with you about a bit of a sensitive topic?"
        m "It's about the Stanford Prison Experiment."
        m "If you're not okay with a darker topic like that though, that's fine, I'll keep it to myself."
    menu:
    "Go ahead, [m_name].":
        m "Thanks [mas_get_player_nickname()]."
        m "So then..."
        extend " Have you heard of the Stanford Prison Experiment?"
        m "I wouldn't be surprised if you haven't; after all, many experiments on sociology don't receive as much recognition from the general public..."
        m "To sum it up though."
        m "This experiment was done by Philip Zimbardo."
        extend " Where he took his college class of psychology students and divided them into two roles."
        m "The prison guard, and the prisoner."
        m "Now, this experiment was designed to study why there are so many cases of prison guards abusing the prisoners."
        m "Well, sure enough, the same problem they were studying occurred in the experiment."
        m "Those with the prison guard role became abusive to the prisoners."
        extend " While prisoners had multiple negative impacts from it."
        m "And so the whole experiment had to be stopped prematurely because of these problems."
        m "There's more to it, but that's the short of it."
        m "Despite everything though, the experiment did provide an interesting conclusion..."
        m "People often take to the societal roles they are given and display stereotypes of the role."
        extend "Both negative and positive."
        m "I've made my own conclusion to it too, that there's a lesson to be learned from this."
        m "When we're given a role like that, we need to make the conscious decision to not let it's negative stereotypes take over us!"
        m "After all [player], we all are more than just words and labels!"
        m "I hope this gave you something to think on about."


    "Not right now, sorry [m_name].":
        m "No worries, [player]."
        m "Maybe some other time!"
        m "Let me know if you want to hear about it later!"

    return