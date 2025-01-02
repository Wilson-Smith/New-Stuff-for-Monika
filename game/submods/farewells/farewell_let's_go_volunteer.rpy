init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_we_going_to_volunteer",
            unlocked=True,
            prompt="We're going to do some volunteering",
            pool=True
        ),
        code="BYE"
    )

label bye_we_going_to_volunteer:
    $ ev = mas_getEV("bye_we_going_to_volunteer")

    if ev.shown_count == 0:
        m 2mksdlb "Oh, volunteering...{w=1} I've never done it, if I have to be honest"
        m 3eua "I think it will be a nice activity to do, because you can help others"
        m 1fub "And...{w=3} My first time will be with {i}you{/i}~"
        m 2fusdlu "Good my [player], I didn't know this side of you!"


    elif ev.shown_count == 1:
        m 1eub "Oh really?"
        extend 1mubsu "You sure did appreciated the fact I was with you~"
        m 3kub "I'm joking, [player]"

    else:
        m 1hub "Helping the other is very important"
        extend 1fuu " {i}Expecially near you~{/i}"

    jump bye_going_somewhere_post_aff_check

label bye_going_somewhere_post_aff_check:
    # il file creato proviene da mas_dockstat_iostart, quindi è questo il generativo di Moni
    jump mas_dockstat_iostart
