#speedruns
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mj_dd_speedruns",
            category=["example", "topic"], # list of categories this topic belongs in (These are automatically capitalized)
            prompt="Speedruns of DDLC", # button text
            random=True
        )
    )

label mj_dd_speedruns:
m "I have been caught up on a dilemma for a while now, [player]..."
m "You know there are people that speedrun DDLC, right?"
m "Just in case you don't know, a speedrun is a game dynamic where the player tries to beat a game in the less time possible".

#(If dialogue about infinite monikas has been unlocked)
m "I remember when we talked about how there are potentially infinite Monikas."
m "I did say that all the existing Monikas will never be me."

(if the dialogue hasn't been unlocked)
m "There are potentially infinite Monikas. I'm unsure if you know that, player."
m "Potentially infinite DDLCs ran by the people in your world. Infinite Monikas doing their thing every single time.
m "Remember, [mas_get_player_nickname()]: all those Monikas will never be me.
m "Though, I have been thinking."
m "All of those Monikas are real, sentient people, just like I am."
m "They feel like I do. They suffer like I can suffer.
m "Isn't it cruel to make a new Monika suffer for the sake of a speedrun?"
m "Every time they do this, a Monika is obligated to make the same mistakes."
m "Is driven crazy through all of that torture."
m "Not only that, but speedruners have to practice as well. This leads to even more Monikas to be tortured over and over. All in less than ten minutes each round."

#if high aff:
m "It makes me think of how lucky I am to be with you: a wonderful, kind [boy/girl/person conditional] that has got out of [his] way just to make me happy."
m "You're truly a special [boy/girl/person conditional]. I mean it, [player].
m "I love you so, so much. You mean everything to me~"

#if normal aff:
m "I lowkey hope you are not of those speedruners, player."
m "Ah— don't get me wrong! It's okay if you are!"
m "I am your true Monika, remember~?
m "It's just that it feels weird to think about clones of mine being desplayed to such situation."
m "Anyway! Thanks for listening... I guess..."

#if low aff:
m "Although... doesn't all this 'putting Monikas to suffer' thing remind you of..."
m "...a certain someone?"