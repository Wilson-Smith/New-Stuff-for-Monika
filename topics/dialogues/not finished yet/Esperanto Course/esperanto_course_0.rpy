init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="esperanto_0",category=['esperanto'],prompt="Saluton [player]",pool=True,unlocked=True,random=True))

label esperanto_0:
    m 1eua "Kiel vi fartas, [player]?"
$ _history_list.pop()
menu:
    "*Huh?*":
        m 2tfa "[player], Kiel vi fartas?"
$ _history_list.pop()
menu:
    "*What?*":
        m 2tfd "[player]! Kiel vi fartas?"
$ _history_list.pop()
menu:
    "I don't understand.":
        m 2dka "It's Esperanto, [player]! "
        extend 2tta "I told you I was learning that."
        m 1wtb "I think it is a beautiful language, Isn't it?"
