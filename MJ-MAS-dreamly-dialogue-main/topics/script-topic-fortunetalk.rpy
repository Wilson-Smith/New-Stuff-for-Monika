#Fourtune time
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mj_dd_fourtune_time",
            category=["example", "topic"], # list of categories this topic belongs in (These are automatically capitalized)
            prompt="Fortune", # button text
            aff_range=(mas_aff.ENAMORED, None),
            random=True
        )
    )

label mj_dd_fourtune_time:
    m "[player]! I have a surprise for you!"
    m "I’m going to read your fortune!"
    m "Ahaha! I know it might seem random but, I just made this paper fortune teller and I want to test it out!"
    m "Okay, here we go!"
    m "…"
    m "Aha! It says, You are going to receive a cute surprise!"
    call monika_kissing_motion_short
    m "Looks like your fortune came true, ahaha~"
return
