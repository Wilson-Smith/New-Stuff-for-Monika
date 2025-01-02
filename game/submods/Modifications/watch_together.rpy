#ver 1.2.0
#update notes: added affection gain, added "watch me code", added brb to tell monika you're going to watch something by yourself

# This submod was made by u/geneTechnician, changes by u/WilsonSmith01

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="doing_something_brb",
            category=["be right back"],
            prompt="I'm going to do stuff",
            pool=True,
            unlocked=True,

        ),
    )

label doing_something_brb:
    $ ev = mas_getEV("doing_something_brb")

    if ev.shown_count == 0:
        m 1eud "Oh,{w=0.1} really?"
        m 3rksdla "Well, I could do something with you if you wanted me to."
        m 2ekbla "It would be a nice way to spend time together next time."

    else:
        m 1eub "Okay, [mas_get_player_nickname()]."
        m 3eua "I'll be here when you get back."

$ mas_idle_mailbox.send_idle_cb("doing_something_brb_callback")
return "idle"

label doing_something_brb_callback:
    m 1hub "Welcome back!"
    m 2eua "I hope you had fun."
    m 2lkblsdru "I'd be lying if I said I wasn't happy you're back spending time with me again, though."
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="doing_things_together",
            random=True,
            pool=False,
            aff_range=(mas_aff.HAPPY, None)

        ),
    )

label doing_things_together:

    m 3eua "Did you know that I can watch things with you?"
    m 4esb "All you have to do is make sure the 'Fullscreen' option is unchecked in the settings menu."
    m 1eub "That will let you resize the game's window so you can place me next to the video player."
    m 1hub "Or next to whatever else you might want to show me!"
    m 7eua "Then,{w=0.1} you should look up the 'Do you want to do something with me?' topic to let me know that we're going to be..."
    m 7hksdrb "Well,{w=0.1} doing something!{w=0.3} Ahaha."
    m 2ekblsdra ".{w=0.1}.{w=0.1}."
    m 5rkbfsdru "I just thought it might be a nice way to spend time together."
    
return "derandom"

default -5 persistent._mas_taking_break_from_watching = None
default -5 persistent._mas_watching_you_draw = None
default -5 persistent._mas_watching_you_game = None
default -5 persistent._mas_watching_you_code = None
default -5 persistent._mas_watching_you_homework = None
default -5 persistent._mas_watching_you_write = None

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="doing_together",
            category=["us"],
            prompt="Do you want to do something with me?",
            pool=True,
            unlocked=True,
            aff_range=(mas_aff.HAPPY, None),
        ),
    )

label doing_together:

    if persistent._mas_taking_break_from_watching:
        m 3eua "Ready to keep going, [mas_get_player_nickname()]?"
        m 7hub "I know I am!"
    else:
        $ mas_gainAffection(3, bypass=False)
        m 1hub "Of course!"
        m 7eua "What did you have in mind?{nw}"

        $ _history_list.pop()
        menu:
            m "What did you have in mind?{fast}"
            
            "Watch me write something":
                m 1eub "Oh, what are you writing?"
                $ _history_list.pop()
                menu:
                    "Poetry":
                        if persistent._mas_pm_has_poetry_experience is False:
                            m 1wuo "I thought you didn't write poetry?" 
                            m 1sub "Did you start learning for me?{w=0.3}{nw} "
                            extend 1fkbsa "You're so sweet~"
                            m 1lub "If you need some help with the grammar you can check the 'Grammar Tips' section "
                            extend 1rub "and the 'Poetry Tips' section."
                            m 7eua "You might want to go back to the 'Poetry experience' topic and update your answer so I'll remember next time."

                        else:
                            m 1eub "I wonder what you're going to focus on."
                            m 3eub "I hope it's on me!{w=0.3}"
                            m 1hubssdlb "...{w=3.0}{nw}"
                            extend 1fsbfu ""
                            m 3rsbsb "However that's will be one of my favourites for sure"
                            m 1hublu "Ehehe~"
 
            "Reading":
                $ persistent._mas_watching_you_draw = False
                $ persistent._mas_watching_you_game = False
                $ persistent._mas_watching_you_code = False
                m 2eub "Sounds fun."
                m 1rtc "I wonder witch genre you're reading and more into..."
                m 3rua "Sci-Fi? Horror? Poetry? Science? or maybe...{w=0.3}{nw}"
                extend 1tsblu "Romance?"
                m 1hublu "Ehehe~"
                
            "Watch me doing my homework":
                $ persistent._mas_watching_you_draw = False
                $ persistent._mas_watching_you_game = False
                $ persistent._mas_watching_you_code = False
                m 2eub "Ok!"

            "A movie/TV show":
                $ persistent._mas_watching_you_draw = False
                $ persistent._mas_watching_you_game = False
                $ persistent._mas_watching_you_code = False
                m 1rtc "Hm,{w=0.3} I wonder what the genre is going to be..."
                m 3rua "Action? Horror? Or maybe...{w=0.3}{nw}"
                extend 1tsblu "Romance?"
                m 1hublu "Ehehe~"

            "Youtube videos/Twitch stream":
                $ persistent._mas_watching_you_draw = False
                $ persistent._mas_watching_you_game = False
                $ persistent._mas_watching_you_code = False
                m 2eub "That sounds fun!"
                m 4eua "Letting yourself watch mindless things online for awhile isn't always a bad thing."
                m 3hublb "And if it lets us spend more time together, that's even better!"

            "Watch me draw":
                $ persistent._mas_watching_you_draw = True
                $ persistent._mas_watching_you_game = False
                $ persistent._mas_watching_you_code = False
                m 2sublo "Really?"
                m 3ekbla "I know sharing your art with other people can be really difficult sometimes."
                m 1ekbsu "So the fact you trust me enough to share it with me,{w=0.3} even when it's unfinished,{w=0.1} means a lot to me."

            "Watch me code":
                $ persistent._mas_watching_you_code = True
                $ persistent._mas_watching_you_draw = False
                $ persistent._mas_watching_you_game = False

                if persistent._mas_pm_has_code_experience is False:
                    m 3etd "I thought you didn't know how to code?"
                    m 1sub "Did you start learning for me?{w=0.3}{nw} "
                    extend 1hubsu "You're so sweet~"
                    m 7eua "You might want to go back to the 'Coding experience' topic and update your answer so I'll remember next time."
                else:
                    m 1rud "I wonder what you're going to be working on, or what language you're using."
                    m 3eub "I hope it's Python!{w=0.3}{nw} "
                    extend 1hub "That's my favorite~"

            "Watch me play a game":
                $ persistent._mas_watching_you_game = True
                $ persistent._mas_watching_you_draw = False
                $ persistent._mas_watching_you_code = False
                m 1tua "Oh?{w=0.3}{nw} " 
                extend 3gtb "Are you trying to show off in front of your cute girlfriend?"
                m 1hublu "Ehehe~{w=0.3} I'm just teasing you, [mas_get_player_nickname()]."
            

        m 2eub "Alright,{w=0.3} go ahead and do whatever you need to do to get set up."
        m 7esa "I'm going to put a choice on screen so you can let me know when you're ready."

        $ _history_list.pop()
        menu:

            "I'm ready!":
                m 1hua "Great!"

        if persistent._mas_watching_you_draw:
            m 1sub "I can't wait to see what you end up drawing!"
        elif persistent._mas_watching_you_code:
            m 7eub "Make sure to keep your code organized and easy to read!"
        elif persistent._mas_watching_you_game:
            m 3huu "I'll be cheering you on!"
        else:
            m 1eub "Let me know when you want to stop or take a break, okay?"

$ mas_idle_mailbox.send_idle_cb("watching_something_callback")
return "idle"

label watching_something_callback:
    m 3eud "Are you ready to stop for now?{nw}"

$ _history_list.pop()
menu:
    m "Are you ready to stop for now?{fast}"

    "Yeah.":
        $ persistent._mas_taking_break_from_watching = False
        m 1hua "Alright!"
        m 3lsblb "I hope we get to do this again soon."
        m 5ekbsu "I always love spending time with you, [player]."

    "I'm taking a quick break.":
        $ persistent._mas_taking_break_from_watching = True
        m 1hua "Alright!"
        m 7eub "Just go back to the 'Do you want to watch something with me?' topic to let me know when you're ready to keep going."
return