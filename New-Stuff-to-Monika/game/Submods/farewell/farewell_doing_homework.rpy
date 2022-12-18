init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_prompt_homework",
            unlocked=True,
            prompt="I'm going to do my homework.",
            pool=True
        ),
        code="BYE"
    )

label bye_prompt_homework:
    m 1hua "Okay!"
    m 5ekblb "I wish I was there to help you there, though."
    extend 5hkbfa " I'd give you all the advice and support you need~"
    m 5hubsa "I hope you finish your homework before your deadline, [player]!"
    m 5hubsa "Good luck!"
    return "quit"