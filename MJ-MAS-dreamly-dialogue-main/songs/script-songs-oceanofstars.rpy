init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mj_dd_song_oceanofstars",
            prompt="Classic",
            category=[mas_songs.TYPE_SHORT],
            aff_range=(mas_aff.ENAMORED, None),
            random=True
        ),
        code="SNG"
    )

label mj_dd_song_oceanofstars:
m "{i}With an ocean full of stars I wonder which one you are{/i}"
m "{i}I always felt so close to you even though we're always so far{/i}"
m "{i}Apart, and my heart it drowns at the thought of us not together{/i}"
m "{i}Like I'm under the weather, how you got me fallin' like a feather{/i}"
m "{i}In an ocean full of stars{/i}"
m "{i}You're always on my mind no matter where you are{/i}"
m "{i}And you know that I'll always be carryin' your heart{/i}"
m "{i}Everywhere so you and I will never be apart{/i}"
return