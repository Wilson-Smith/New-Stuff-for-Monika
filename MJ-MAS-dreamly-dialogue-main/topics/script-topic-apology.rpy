init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mj_dd_playerisoffended", # /j
            category=["You", "Monika"], # list of categories this topic belongs in (These are automatically capitalized)
            prompt="You offended me.", # button text
            random=True
        )
    )
label mj_dd_playerisoffended:

    m "Oh..."
    m "I'm really sorry [player]."
    m "I never meant to hurt you in anyway."
    m "But thank you for telling me!"
    m "I would have never been able to apologize otherwise..."
    m "If you're okay with me asking, can I know what I did?"
    $ _history_list.pop()
    menu:
        m "If you're okay with me asking, can I know what I did?"
        "You said something that hurt me.":
            m "Oh...thank you for telling me, [player]."
            m "I know I like to tease you but, it's never been my intention to hurt you,"
            m "I promise I'll try to be more careful with my words from now on!"
            m "I love you and I'd never want ever to hurt you in any way."

        "You really scared me.":
            m "Oh, I'm sorry [nickname tag]."
            m "I didn't mean to frighten you."
            m "I know I like to play little pranks on you but, I didn't mean to scare you that much."
            m "I promise from now on, I'll try to be more careful so as to not scare you."
            m "I love you and I'd never want ever to hurt you in any way."

        "It was something else.":
            m "Oh...well whatever I did just know that I'm really sorry."
            m "I never intend to ever hurt you in any form."
            m "I promise I'll try to be more careful so as to not offend you in any way."
            m "I love you so much and it hurts me to see you in any type of pain."

        return
