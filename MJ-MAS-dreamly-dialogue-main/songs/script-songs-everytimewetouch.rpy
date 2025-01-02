init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mj_dd_song_every_time_we_touch",
            prompt="Everytime We Touch",
            category=[mas_songs.TYPE_LONG],
            aff_range=(mas_aff.ENAMORED, None),
            random=True
        ),
        code="SNG"
    )

label mj_dd_song_every_time_we_touch:
    m "{i}I still hear your voice when you sleep next to me.{/i}"
    m "{i}I still feel your touch in my dreams.{/i}"
    m "{i}Forgive me my weakness..{/i}"
    m "{i}But I don't know why.{i}"
    m "{i}Without you it's hard to survive~{i}"
    m "{i}'Cause everytime we touch, I get this feeling!{i}"
    m "{i}And every time we kiss. I swear I could fly~{i}"
    m "{i}Can't you feel my heart beat fast?{i}"
    m "{i}I want this to last..{i}"
    m "{i}Need you in my life."
    m "{i}'Cause every time we touch..~{i}"
    m "{i}I feel the static."
    m "{i}And every time we kiss, I reach for the sky~{i}"
    m "{i}Can't you hear my heart beat so?"
    m "{i}I can't let you go!~"
    m "{i}Want you in my life.."
    m "{i}Your arms are my castle."
    m "{i}Your heart is my sky.."
    m "{i}They wipe away tears that I cry.."
    m "{i}Oh, the good and the bad times.."
    m "{i}We've been through them all."
    m "{i}You make me rise when I fall~"
    m "{i}'Cause every time we touch~~"
    m "{i}I get this feeling~"
    m "{i}And every time we kiss I swear I could fly!~"
    m "{i}Can't you feel my heart beat fast?"
    m "{i}I want this to last~"
    m "{i}Need you by my side.."
    m "{i}'Cause every time we touch."
    m "{i}I feel the static~"
    m "{i}Every time we kiss."
    m "{i}I reach for the sky!~"
    m "{i}Can't you feel my heart beat, so?"
    m "{i}I can't let you go.."
    m "{i}Want you in my life."
    m "{i}Every time we touch..~"
    m "{i}I get this feeling.."
    m "{i}Every time we kiss I swear I could fly.."
    m "{i}Can't you feel my heart beat fast?"
    m "{i}I want this to last~"
    m "{i}Need you by my side."
    m "{i}'Cause every time we touch.."
    m "{i}I feel the static~"
    m "{i}Every time we kiss."
    m "{i}I reach for the sky..~"
    m "{i}Can't you feel my heart beat so?"
    m "{i}I can't let you go~"
    m "{i}Want you in my life..~"
    m "Everything in this song is true, [player]..."
return
#Reminder to add the italics-