init python:
    addEvent(Event(persistent.event_database,eventlabel="esperanto_1",category=['esperanto', 'languages'],prompt="Esperanto 1",pool=True,unlocked=True,random=False))
label esperanto_1:
    m 1eua "Hello [player], this is the first Esperanto lesson. {w=0.6} I'm going to teach you how to say greet someone in Esperanto."
    m 1eub "First, I'm going to teach you how to say hello."
    extend 3eub " In Esperanto, you say 'Saluton' to someone to say hello. It's very simple."
    m 4eua "Ok, now let's say 'Thanks' in Esperanto."
    extend 7eub " In Esperanto, you say 'Dankon' to someone to say thanks."
    m 2eua "Ok, now let's say 'Goodbye' in Esperanto."
    extend 1eua " In Esperanto, you say 'Adiaŭ' to someone to say goodbye."
    m 7eub "Ok, now let's say 'How are you' in Esperanto."
    extend 7eua " In Esperanto, you say 'Kiel vi faras?' to someone to say how are you."
    m 1hua "That's enought for today"
    extend 1kua " If you want, there is a topic called 'Esperanto Training 1'"

init python:
    addEvent(Event(persistent.event_database,eventlabel="esperanto_training_1",category=['esperanto', 'languages'],prompt="Esperanto Training 1",pool=True,unlocked=True,random=False))
label esperanto_training_1:
    m 1eub"After the first lesson, let's train a little bit."
    m 3esblb "'Saluton' is 'Hello' in Esperanto?"
    
    while True:
        menu:
            "Yes.":
                m 1hsblb "Good job, [player]! You're doing great!"
                m 7esa "Now, let's go to the next question."
                m 4esb "In Esperanto, how can we say 'how are you?'"
                python:
                    break
            "No.":
                m 1tkp "Oh, that's not correct. Let's try again."
                m 3esblb "'Saluton' is 'Hello' in Esperanto?"

    while True:
        menu:
            "Kiel vi fartas?":
                m 1hsblb "Good job, [player]! You're doing great!"
                m 1esa "Now, let's go to the next question."
                m 3esb "How can we say 'goodbye' in Esperanto?"
                python:
                    break
            "Kiel mi fartas?":
                m 1dsb "Concentrate [player]!"
                m 1esb "it is 'Kiel vi fartas', not 'Kiel mi fartas'"
                extend 1eud "The latter means 'How am I'! Let's try again."
                m 4esb "In Esperanto, how can we say 'how are you?'"

    while True:
        menu:
            "Adiau":
                m 3dua "Concentrate [player], you can do it! Let's try again."
                m 3esb "How can we say 'goodbye' in Esperanto?"

            "Adiaŭ":
                m 1hsblb "Good job, [player]! You're doing great!"
                m 7esa "Now, let's go to the next question."
                m 4esb "Is 'Dankon' 'Thanks' in Esperanto?"
                python:
                    break

    while True:
        menu:
            "Yes.":
                m 1hsblb "Good job, [player]! You're doing great!"
                python:
                    break
            "No.":
                m 2ekd "Oh, that's not correct. Let's try again."
                m 4esb "Is 'Dankon' 'Thanks' in Esperanto?"

    m 1eub "Anyway, I suggest you to exercise a little more, [player]~"

# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
