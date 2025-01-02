#Hand written notes
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mj_dd_handwriting",
            category=["example", "topic"], # list of categories this topic belongs in (These are automatically capitalized)
            prompt="Hand Written Notes", # button text
            random=True
        )
    )

label mj_dd_handwriting:
m "[player], you know what saddens me?"
m "That someday people will no longer be using handwritten notes…"
m "Now I know this sounds a little silly, but it actually really hurts me when I think about it."
m "Whenever I received a handwritten note, I would always keep it in a little box."
m "I always loved going back and rereading them when I felt sad or hurt."
m "There was just something about knowing that someone cared for me enough to take the time out of their day to write me something."
m "It didn’t matter the size or length, just the fact that they did it."
m "Also, I always loved seeing their handwriting and knowing it actually came from them."
m "Messy or neat, I loved them all dearly."
m "You see [player], oftentimes handwritten notes and letters are better than typed because, it’s personal!"
m "A lot of people don’t understand why some prefer handwritten stuff because, they don’t understand that it’s because, when you are given something written there’s a certain level of personality that you don’t get with typed documents."
m "Wait! I just got an idea [player]!"
m "What if when I get into your reality, we write each other little notes, every once in a while!"
m "I think it would be really fun!"
m "And then there will always be proof that we both love each other!"
return
