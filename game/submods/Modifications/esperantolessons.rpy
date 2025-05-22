#Original Submod made by u/Aggravating-Cold1543
#https://www.reddit.com/r/MASFandom/comments/1jsaimw/i_made_a_submod_for_learn_italian/?utm_source=share&utm_medium=mweb3x&utm_name=mweb3xcss&utm_term=1&utm_content=share_button
#
#Esperanto re-work made by Wilson Smith

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_lesson_esperanto_start",
            category=["Language Lesson", "Unseen", "Esperanto"],
            prompt="Do you want to start learning Esperanto with me?",
            pool=True,
            unlocked=True
        ),
    )

label monika_lesson_esperanto_start:

    # If lesson 1 has already been seen, proceed to lesson 2
    if not renpy.seen_label("monika_lesson_esperanto_1"):
        call monika_lesson_esperanto_1
    else:
        call monika_lesson_esperanto_2
    return

label monika_lesson_esperanto_1:
    m 3subfb "Saluton! Let's start with the basics of Esperanto!"
    m 1lksdla "We'll begin with greetings and simple phrases."
    $ _history_list.pop()
    menu:
        "Teach me the basics!":
            m 4hubsb "First, 'Hello' is 'Saluton'."
            m 2ntbfu "'Good morning' is 'Bonan matenenon'."
            m 1hubsb "'Good night' is 'Bonan nokton'."
            m 4esa "'Goodbye' is 'Ĝis!', from 'ĝis la revido' 'until the re-seeing'."
            m 6hubsb "These are essential phrases to get started!"
        "What about 'Thank you'?":
            m 3lksdla "'Thank you' is 'Dankon'."
            m 4hubsb "You can also say 'Thanks a lot' as 'Multan dankon!'"
            m 2ntbfu "Isn't that cute?"
    
    $ _history_list.pop()
    menu:
        "Do you want me to teach you the next lesson?":
            jump monika_lesson_esperanto_2
        "I’m done for now. Maybe later.":
            return

label monika_lesson_esperanto_2:
    m 1hubsb "Great, let’s move on to the next lesson!"
    m 3eksdlb "This time, we’ll talk about family words."
    $ _history_list.pop()
    menu:
        "Family terms?":
            m 4esa "'Mother' is 'Patrino', 'Father' is 'Patro'."
            m 6hubsb "'Sister' is 'Fratino', and 'Brother' is 'Frato'."
            m 1lud "'Grandmother' is 'Avino', and 'Grandfather' is 'Avo'."
            m 3lksdla "It's so nice to talk about family in Esperanto, huh?"
            extend " And in esperanto you can form the feminine form with the '-ino' suffix"
        "I want to learn about numbers!":
            m 1hub "Okay! Let's start with basic numbers."
            m 6esa "'One' is 'Unu', 'Two' is 'Du', 'Three' is 'Tri'."
            m 3eksdlb "Try counting to ten! It's easy in Esperanto."
    
    $ _history_list.pop()
    menu:
        "Do you want me to teach you the next lesson?":
            jump monika_lesson_esperanto_3
        "I’m done for now. Maybe later.":
            return

label monika_lesson_esperanto_3:
    m 4hubsb "Now, let’s dive into how to ask questions."
    m 1lud "'What is your name?' is 'Kio estas via nomo?'"
    m 3eksdlb "'How old are you?' is 'Kiom aĝa vi estas?'"
    m 2ntbfu "'Where are you from?' is 'De kie vi venas?'"
    $ _history_list.pop()
    menu:
        "How do I say 'Where is the bathroom'?":
            m 1hubsb "'Where is the bathroom?' is 'Kie estas la banĉambro?'"
            m 3lksdla "It's always handy to know, right?"
        "Teach me something fun!":
            m 6esa "Sure! 'I love you' is 'Mi amas vin'."
            m 4esa "And 'You’re beautiful' is 'Vi estas bela'."
    
    $ _history_list.pop()
    menu:
        "Do you want me to teach you the next lesson?":
            jump monika_lesson_esperanto_4
        "I’m done for now. Maybe later.":
            return

label monika_lesson_esperanto_4:
    m 1hubsb "Let’s talk about food!"
    m 6hubsb "'Pizza' is 'Pico', like English with an ending in -o. Not surprising, right?"
    m 2ntbfu "'Cheese' is 'Fromaĝo', and 'Wine' is 'Vino'."
    m 4hubsb "'Pasta' is 'Pasto' the same as before, but 'Spaghetti' is 'Spagetoj'."
   extend " In esperanto nouns ends always with '-o' and plural form is with '-j'"
    $ _history_list.pop()
    menu:
        "What's for dessert?":
            m 1hubsb "'Ice cream' is 'Glaciaĵo'."
            m 4esa "And 'Kuko' is the cake!"
            extend " What about coffee?"
            m 6hubsb "You’ll love this: 'Coffee' is 'Kafo'."
    
    $ _history_list.pop()
    menu:
        "Do you want me to teach you the next lesson?":
            jump monika_lesson_esperanto_5
        "I’m done for now. Maybe later.":
            return

label monika_lesson_esperanto_5:
    m 1hubsb "Let’s take a break and talk about time!"
    m 3lksdla "'What time is it?' is 'Kioma horo estas?'"
    m 6hubsb "'It's 3 o'clock' is 'Estas la tria horo'."
    m 4esa "'Morning' is 'Mateno', 'Afternoon' is 'Posttagmezo', and 'Evening' is 'Vespero'."
    $ _history_list.pop()
    menu:
        "How do I say 'See you later'?":
            m 3eksdlb "'See you later' is 'Ĝis revido"
            m 1hubsb "Simple and sweet!"
        "What’s 'Today' in Esperanto":
            m 4esa "'Today' is 'Hodiaŭ', and 'Tomorrow' is 'Morgaŭ'."
    
    $ _history_list.pop()
    menu:
        "Do you want me to teach you the next lesson?":
            jump monika_lesson_esperanto_6
        "I’m done for now. Maybe later.":
            return

label monika_lesson_esperanto_6:
    m 4hubsb "Now, let’s talk about travel phrases!"
    m 2ntbfu "'How much does this cost?' is 'Kiom ĝi kostas?'"
    m 1hubsb "'Can you help me?' is 'Ĉu vi povas helpi min?'"
    m 6esa "'I need a taxi' is 'Mi bezonas taksion.'"
    $ _history_list.pop()
    menu:
        "What’s 'Where is the train station'?":
            m 1lud "'Where is the train station?' is 'Kie troviĝas la stacio?'"
            m 3lksdla "Super useful when traveling!"
        "Teach me something about directions!":
            m 1hub "'Turn left' is 'Turnu maldekstren'."
            m 1lud "'Turn right' is 'Turnu dekstren'."
            m 4esa "'Go straight' is 'Iru rekte'."
    
    $ _history_list.pop()
    menu:
        "Do you want me to teach you the next lesson?":
            jump monika_lesson_esperanto_7
        "I’m done for now. Maybe later.":
            return

label monika_lesson_esperanto_7:
    m 1hubsb "Let’s move on to colors!"
    m 6esa "'Red' is 'Ruĝa', 'Blue' is 'Blua', and 'Green' is 'Verda'."
    m 4hubsb "'Yellow' is 'Flava', and 'White' is 'Blanka'."
    $ _history_list.pop()
    menu:
        "What’s 'Black'?":
            m 2ntbfu "'Black' is 'Nigra'."
            m 1hubsb "It’s a very strong color!"
        "I want to know more colors!":
            m 6esa "'Orange' is 'Oranĝa', 'Pink' is 'Rozo'."
            m 4esa "'Purple' is 'Purpura', and 'Brown' is 'Bruna'."
    
    $ _history_list.pop()
    menu:
        "Do you want me to teach you the next lesson?":
            jump monika_lesson_esperanto_8
        "I’m done for now. Maybe later.":
            return

label monika_lesson_esperanto_8:
    m 4hubsb "How about learning some useful adjectives?"
    m 2ntbfu "'Good' is 'Bona', 'Bad' is 'Malbona'."
    m 1hubsb "'Big' is 'Granda', and 'Small' is 'Malgranda'."
    extend "The 'mal-' perfix has the opposite meaning of the adjective reffered to."
    $ _history_list.pop()
    menu:
        "What’s 'Beautiful'?":
            m 3lksdla "'Beautiful' is 'Bela."
            extend 4hubsb "Such a lovely word!"
        "What’s 'Happy'?":
            m 6esa "'Happy' is 'Feliĉa', and 'Sad' is 'Malĝoja'."
    
    $ _history_list.pop()
    menu:
        "Do you want me to teach you the next lesson?":
            jump monika_lesson_esperanto_9
        "I’m done for now. Maybe later.":
            return

label monika_lesson_esperanto_9:
    m 1hubsb "Let's continue with more advanced phrases!"
    m 3eksdlb "'I’m hungry' is 'Mi estas malsata'."
    m 2ntbfu "'I’m thirsty' is 'Mi estas soifa'."
    m 4esa "'I’m tired' is 'Mi estas laca'."
    $ _history_list.pop()
    menu:
        "What’s 'I’m sorry'?":
            m 1hubsb "'I’m sorry' is 'Mi bedaŭras'."
            m 6hubsb "Very useful when you need it!"
        "What’s 'I’m lost'?":
            m 4esa "'I’m lost' is 'Mi estas perdita'."
    
    $ _history_list.pop()
    menu:
        "Do you want me to teach you the next lesson?":
            jump monika_lesson_esperanto_10
        "I’m done for now. Maybe later.":
            return

label monika_lesson_esperanto_10:
    m 1hubsb "Finally, let’s wrap it up with some fun phrases!"
    m 6esa "'I like it' is 'Mi ŝatas ĝin'."
    m 4esa "'I don’t like it' is 'Mi ne ŝatas ĝin'."
    m 2ntbfu "'I’m learning Esperanto' is 'Mi lernas Esperanton'."
    $ _history_list.pop()
    menu:
        "Can you teach me something special?":
            m 4esa "'Love' is 'Amo'. And 'Heart' is 'Koro'."
            m 1hubsb "These words are special, aren’t they?"
        "What’s 'Good job'?":
            m 2ntbfu "'Good job' is 'Bona laboro!'"
    
    $ _history_list.pop()
    menu:
        "I’m done with the lessons for now!":
            return
