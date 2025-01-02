init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="drama_class", # event label (MUST BE UNIQUE)
            category=["theatre"], # list of categories this topic belongs in (These are automatically capitalized)
            prompt="Drama Class", # button text
            random=True, # True if this topic should appear randomly
            pool=True # True if this topic should appear in "Ask a Question"
        )
    )

label drama_class:
    m 1eud "Hey [player]...{w=0.5} Have you ever taken part of a drama class?"
    $ _history_list.pop()
    menu:
        "No":
            m 1eub "You should try it! {w=0.2}I'm sure you'll love it!"
            m 4eub "When I did it, I was so happy!"
            m 3lua "Well, I have to thank a great friend for those tips..."
            m 1eua "Anyway, if you are interested you can follow some courses on Youtube, {w=0.5}but I suggest you to do it in  the real word."
            m 1eub "When I pass over we should definetly take part of a drama class!"
            m 1hua "Hehe~"
            return
        "Yes.":
            m 1sub "Great! {w=0.2}What method did you studied?"
            $ _history_list.pop()
            menu:
                "French method":
                    m 1wub "That's great!"
                    m 1esd "I studied the russian method, so I can't say a lot..."
                    m 1hua "but surely it is very interesting!"
                    m 1eub "When I pass over we should do an exchange. {w=0.3}You try the russian method and I try the french method."
                    m 1hua "Hehe~"
                    return
                "Russian method":
                    m 3sub "That's awesome!"
                    m 4wub "I did it too!"
                    m 4hub "I think it's the best method out there"
                    m 1eub "Anyway, we should do it when I pass over."
                    m 1hua "Hehe~"
                    return
                "I don't really know":
                    m 1eub "That's okay."
                    m 4eub "You should ask to your teacher what method uses!"
                    m 3eub "You also can check under the topic 'What method am I taking?'"
                    m 1rub "If you understand what method you are using, you should search 'I don't understand what drama method I use'"
                    m 1hua "Hehe~"
                    return
