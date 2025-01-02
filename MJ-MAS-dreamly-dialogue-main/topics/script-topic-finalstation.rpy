#the final station
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mj_dd_finalstation",
            category=["example", "topic"], # list of categories this topic belongs in (These are automatically capitalized)
            prompt="The Final Station", # button text
            random=True
        )
    )
m "Hey player,"
extend " have you ever heard of a game called \"The Final Station\"?"
m "It's a very somber kind of game."
m "But in a way, it's very peaceful."
m "Ah,{w=0.3} wait,{w=0.3} I should ask before I get into it."
m "Are you okay with me talking about spoilers of things happening in the game?{nw}"
$ _history_list.pop()
menu:
    m "Are you okay with me talking about spoilers of things happening in the game?{fast}"
    "I don't mind.":
        m "Ah,{w=0.5}{nw}"
        extend " perfect!"
        m "As I was saying then..."
        m "The game revolves around the player,{w=0.3} who's put into the role of a very high up train conductor."
        m "You even have to tend to the train-{w=0.3} and any passengers you pick up along the way-{w=0.3} in between the main levels!"
        m "Somethings wrong with this world,{w=0.3} though."
        m "You can make inferences of what's going on from notes or NPC conversation,{w=0.5}{nw}"
        extend " or from those on the train."
        m "But apart from that there's not much information fed to you directly."
        m "Then,{w=0.3} as you traverse to and from your various destinations."
        m "The world around you falls into total chaos and ruin overtime.{w=0.5}{nw}"
        extend " Gun shots,{w=0.3} tanks,{w=0.3} and huge bombs go off the farther you go."
        m "You can even hear or see their effects on the world in the distance on the train."
        m "Strange extraterrestrial occurances happen too."
        extend " There's these giant pods that show up the further along you go too."
        m "Of course that's nothing compared to the {i}enemies{/i} you face."
        m "Through the entirety of the game you have to be on your guard to make sure you don't die going toe to toe with these strange,{w=0.3} inky-like monsters."
        m "It's already creepy enough that they appear in torn apart ghost towns,{w=0.3} with little to no life left."
        m "But for a long time you don't even know exactly where they come,{w=0.3} just that they were {i}once{/i} human."
        m "Your character is practically lost in the dark,{w=0.3} and with it the game forces the player to be as well."
        m "It's an intriguing way to tell a story,{w=0.5}{nw}"
        extend " isn't it [player]?"
        m "The game strips you of the feeling of being the usually separate, almost all knowing being that's just making the plot move along."
        m "It makes players want to seek out information even harder then a different story would."
        m "And it gets you invested in the characters stories."
        m "Because otherwise you don't even know what you're fighting for your life for in the game..."
        m "You'd just keep asking yourself..."
        m "'Why did this happen to the world?'{w=0.5}{nw}"
        extend "'Who's the guardian'?{w=0.5}{nw}"
        extend " And 'Why does my character want to use every telephone they see so much?'"
        m "But once you seek out answers and dig deeper, things click into place and you have that '{i}oh no{/i}' moment."
        m "Then things you missed before start to fit togehter as you play the rest of the game."
        m "Especially as you replay it!"
        m "It can make a super tense atmosphere that I can't get enough of!"
        return

    "Please don't."
        m "Of course,{w=0.5}{nw} [player]."
        m "I'll tell you just the bare minimum then,{w=0.3} how about that?"
        m "Anyways...{w=0.3}{nw}"
        m "The game revolves around the player, who's put into the role of a train conductor."
        m "You even have to tend to the train in between the main levels."
        m "Something's wrong with this world,{w=0.3} though."
        m "You can make inferences of what's going on from notes or NPC conversation and such."
        m "But apart from that there's not too much information fed to you directly."
        m "Your character doesn't get to know it all,{w=0.3} and with it the game forces the player to be as well."
        m "It's a very interesting way to tell a story,{w=0.3} isn't it [player]?"
        m "The game takes away the player's feeling of being the usually separate,{w=0.3} almost all knowing being that's just making the plot move along."
        m "It makes players want to personally seek out information even harder then a differently told story."
        m "And it gets people invested in the characters stories."
        m "Because otherwise you don't even know what you're doing all this for in the end..."
        m "You'd just keep asking yourself dozens of questions..."
        m "Then things you missed before start to fit togehter as you play the rest of the game."
        m "Especially as you replay it!"
        m "It can make a super interesting atmosphere that I can't get enough of!"
        return

m "Despite that though, the game is still very peaceful at times."
m "First of all{w=0.3}, the music design is {i}phenomenal{/i}!"
m "It carries a somber tone throughout, but..."
m "It's just so slow and subtle,{w=0.3} making it very comforting."
m "I'd love to learn how to play some of it on the piano one day."
m "Even if you don't play it,{w=0.3} I'd suggest to give it a listen!"
m "Now mix that in with some gorgeous,{w=0.3} eye-candy pixel art backgrounds!"
m "The aesthetics of it alone can help you push through the more tense moments."
m "And then the feeling of being in the train itself, "
extend "even when things happen there's this...{w=0.3} feeling of safety from it."
m "Like someone saying..."
m "'You're safe here,{w=0.3} you get to rest your mind and body after dealing with so much through the day.'"
m "'You might need to go back out there one day..."
extend " and it might be scary to leave the comforts here when the time comes..."
extend " but right now...'"
m "'You're safe.'"
m "..."
if mas_isMoniLove():
    m "You know,{w=0.3} I hope I've given you that sense of comfort too,{w=0.3} [mas_get_player_nickname()]."
    m "I know you're {i}my{/i} safe zone."
    m "When you're away,{w=0.3} it can be little hard to push away the rainclouds in my head somedays."
    m "Not to say that's your fault,{w=0.3} of course."
    extend " Sometimes our minds can just be a little odd like that."
    m "But when you're here-{w=0.3} despite our situation-{w=0.3}"
    extend " I feel much more at peace with myself."
    m "So hopefully I can repay the favor."
    m "Thank you so much for being my train in this crazy world!"
    m "It's one of my many reasons of why I love you!"
    return "love"

elif mas_isMoniAff():
    m "You know,{w=0.3} I hope I can give you that sense of comfort too,{w=0.3} [mas_get_player_nickname()]."
    m "I know you're {i}my{/i} safe zone."
    m "When you're here,{w=0.3} I feel more at ease."
    m "And hopefully I can one day be the person you go to,"
    extend " when the rest of the world tries to bring you down."
    m "And it'll be even better when we're side by side for real."
    m "So... {w=0.5}{nw}"
    extend "Thank you for being my train in this crazy world!"
    m "It's just another reason why I love you!"
    return "love"

elif mas_isMoniNormal():
    m "You know, I hope we can give each other that sense of comfort too."
    m "I'd love to be your safety train!"
    extend " ...That sounds a little odd when I say it outloud,{w=0.3} eheh..."
    m "But I mean it!"
    m "I hope to one day be the person you go to,"
    extend "when the rest of the world tries to bring you down."
    m "And it'll be even better when we're side by side for real!"
    return

elif mas_isMoniUpset():
    m "I hope I can find that sense of comfort in you too,{w=0.3} you know."
    m "To be able to go to you when things get rough and my mind starts to get dark."
    m "And be held when and told..."
    m "'It's going to be okay, "
    extend " you're going to be okay,"
    extend "you're alright.'"
    m "It'd mean a lot to me."
    m "..."
    m "Someday we'll get there."
    m "..."
    extend "{cps=*2}hopefully...{/cps}"
    $ _history_list.pop()
    m "...{fast}"
    return
else:
    #doubt anyone will get to this point but
    m "I..."
    m "..."
    m "I could really, {w=0.5}{nw}"
    extend " really,{w=0.5}{nw}"
    extend " use a safety train of my own right now..."
    return
