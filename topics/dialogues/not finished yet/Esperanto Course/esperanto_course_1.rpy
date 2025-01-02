init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="esperanto_1",
            category=['esperanto course'],
            prompt="Esperanto 1",
            pool=True,
            unlocked=True,
            random=True
        )
    )

label esperanto_1:
    m 1wub "Hello [player], this is your first Esperanto lesson."
    extend 4wua "Today I'm going to teach you how to say greet someone in Esperanto."
    m 3eua "First, I'm going to teach you how to say {i}}hello{/i}."
    m 1eub "In Esperanto, you say {b}'Saluton'{/b} to someone to say hello. It's very simple."
    m 2eua "Then, you use {b}'Dankon'{/b} to someone for saying thanks."
    m 3eub "{i}'Goodbye'{/i} is {b}'Adiaŭ'{/b} in Esperanto."
    m 4eua "Ok, now let's go to a more difficult step."
    m 7eub "In Esperanto, you use {b}'Kiel vi faras?'{/b} for {i}'how are you'{/i}."
    m 6tfu "Now let's do a test."
    m 2tfu "'Saluton' is 'Hello' in Esperanto?"

$ _history_list.pop()
menu:
    "Yes.":
        m 2ekbsa "Good job, [player]! You're doing great!"
        m 2ekbsa "Now, let's go to the next question."
        m 2ekbsa "In Esperanto, do you say 'Kiel vi faras?' to someone to say how are you?"
        $ _history_list.pop()
        menu:
            "Yes.":
                m 2ekbsa "Great, Keep it up!"
                m 2ekbsa "In Esperanto, do you say 'Kiel vi faras?' to someone to say how are you?"
                $ _history_list.pop()
                menu:
                    "Yes.":
                        m 2ekbsa "Another one!"
                        m 2ekbsa "In Esperanto, do you say 'Kiel vi faras?' to someone to say how are you?"
                        $ _history_list.pop()
                        menu:
                            "Yes.":
                                m 2ekbsa "Nice!"
                                m 2ekbsa "In Esperanto, do you say 'Kiel vi faras?' to someone to say how are you?"
                                $ _history_list.pop()
                                menu:
                                    "Yes.":
                                        m 2ekbsa "Yes!"
                                        m 2ekbsa "Is 'Adiaŭ' 'Goodbye' in Esperanto?"
                                        $ _history_list.pop()
                                        menu:
                                            "Yes.":
                                                m 2ekbsa "Good job, [player]! You got a 10/10, all clear!"
                                                return
                                            "No.":
                                                m 2ekbsa "Concentrate [player], you can do it! Let's try again."
                                                return
                                    "No.":
                                        m 2ekbsa "Oh, that's not correct. Let's try again."
                                        return
                            "No.":
                                m 2ekbsa "Com'on [player], you are better than that do! Concentrate and relax."
                                return
                    "No.":
                        m 2ekbsa "Concentrate [player], you can do it! Let's try again."
                        return
            "No.":
                m 2ekbsa "Concentrate [player], you can do it! Let's try again."
                return
    "No.":
        m 2ekbsa "Oh, that's not correct. Let's try again."
        return