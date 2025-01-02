init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_prompt_modify",
            unlocked=True,
            prompt="I'm going to modify something.",
            pool=True
        ),
        code="BYE"
    )

label bye_prompt_modify:
    m 1hua "Oh!"
    extend 1hua " What is it not working as expected?"
    $ _history_list.pop()
    menu:
        "Something in your code":
            $ _history_list.pop()
            menu:
                "A Submod":
                    m 1hua "Is it working?"
                    $ _history_list.pop()
                    menu:
                        "Yes, but not as expected.":
                            m 1hua "I hope you can fix it."
                            m 1hua "See you later."
                            return "quit"
                        "No, it isn't working at all!":
                            m 1hua "I'm sorry to hear that"
                            extend hua " I hope you can cope with it."
                            m 1hua "See you later."
                            return "quit"
                        "Yes, it's only a modifcation.":
                            m 1hua "Ok, I'll keep it in mind."
                            m 1hua "See you later."
                            return "quit"
                "A Sprite Pack":
                    m 1hua "Is it working?"
                    $ _history_list.pop()
                    menu:
                        "Yes, but not as expected.":
                            m 1hua "I hope you can fix it."
                            m 1hua "See you later."
                            return "quit"
                        "No, it isn't working at all!":
                            m 1hua "I'm sorry to hear that"
                            extend hua " I hope you can cope with it."
                            m 1hua "See you later."
                            return "quit"
                "A Location":
                    m 1hua "Is it working?"
                    $ _history_list.pop()
                    menu:
                        "Yes, but not as expected.":
                            m 1hua "I hope you can fix it."
                            m 1hua "See you later."
                            return "quit"
                        "No, it isn't working at all!":
                            m 1hua "I'm sorry to hear that"
                            extend hua " I hope you can cope with it."
                            m 1hua "See you later."
                            return "quit"
                "A Dialogue":
                    m 1hua "Is it working?"
                    $ _history_list.pop()
                    menu:
                        "Yes, but not as expected.":
                            m 1hua "Oh, what is the problem?"
                            $ _history_list.pop()
                            menu:
                                "There is a typo in the dialogue.":
                                    m 1hua "I hope you can fix it."
                                    m 1hua "See you later."
                                    return "quit"
                                "There is a missing dialogue.":
                                    m 1hua "I hope you can fix it."
                                    m 1hua "See you later."
                                    return "quit"
                        "No, it isn't working at all!":
                            m 1hua "I'm sorry to hear that"
                            extend hua " I hope you can cope with it."
                            m 1hua "See you later."
                            return "quit"
                "A Game":
                    m 1hua "Is it working?"
                    $ _history_list.pop()
                    menu:
                        "Yes, but not as expected.":
                            m 1hua "I hope you can fix it."
                            m 1hua "See you later."
                            return "quit"
                        "No, it isn't working at all!":
                            m 1hua "I'm sorry to hear that"
                            extend hua " I hope you can cope with it."
                            m 1hua "See you later."
                            return "quit"
        "Something else":
            m 1hua "Oh!"
            extend 1hua " Can I know the problem?"
            $ _history_list.pop()
            menu:
                "I don't know":
                    m 1hua "How unfortunate!"
                    extend 1hua " I'm sorry to hear that."
                    m 1hua "I hope you will cope with this problem."
                    m 1hua "Good Luck!"
                    return "quit"
                "I already know":
                    m 1hua "How unfortunate!"
                    extend 1hua " Can I know the problem?"
                    $ _history_list.pop()
                    menu:
                        "It will be difficult to explain it...":
                            m 1hua "Oh! Ok, then..."
                            m 1hua "Good Luck!"
                            return "quit"