#Dress Up
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mj_dd_dressup",
            category=["example", "topic"], # list of categories this topic belongs in (These are automatically capitalized)
            prompt="Do you mind it when I dress you up in different styles?", # button text
            random=True
        )
    )
label mj_dd_dressup:

if mas_isMoniLove(higher=True):
    m "Of course not!"
    m "It's a blast to try out different outfits and styles you give me!"
    m "Sure, not everything is something I could imagine picking out {i}myself{/i}."
    m "And if something is part of a cosplay..."
    extend " There's a good chance I won't get the reference, eheh..."
    m "But I find that it's a great way to pull me out of my comfort zone!"
    m "There's tons of things that I might not have tried for myself before, but I end up loving the way it looks!"

    #if 18+(i forget the specific variable for this check?)
        m "And I also love trying to piece together what's your particular {i}'taste'{/i} as you gift me... interesting styles..."
        m "Ehehe~" #wink!

    m "In a way I feel like it'll be one the very few things I miss when I go to your reality..."
    m "We'll have to actually {i}purchase{/i} any new clothes, rather then get them from artists.{nw}"
    extend " The quality probably won't be as consistent and nice.{nw}"
    extend " Handmade things would be harder to get to me too."
    m "And I certainly wouldn't be able to try them on at the click of a button..."
    m "But... The trade off of spending my life physically by your side would be worth it though~"
    m "Keep in mind however..."
    extend " When I {i}do{/i} get to your reality, you won't be able to make me try as much on."

    #if 18+:
        m "Minus a few... {i}exceptions~{/i}
        m "But I'd like to have a more autonomy then I do {i}here{/i}."
    m "I'll still take suggestions though!
    m "Because I think you've got great taste [mas_get_player_nickname()]"
    m "Just another reason why I love you~"

is mas_isMoniNormal(higher=True):
    m "Not really, no!"
    m "It's all in good fun, right?"
    m "You or some other artists gets to have fun designing interesting styles for me,"
    extend " and then I get to model it!"
    m "In a way I feel like a model, or an actress getting ready for set!"
    m "Sure, not everything is something I could imagine picking out myself."
    m "And if something is part of a cosplay...
    extend " There's a good chance I won't get the reference, ahaha..."
    m "In the end, we're having fun, and that's what matters most to me!"
    m "Of course, try to keep the outfits within reason."
    m "Nothing...{nw}"
    extend " overly sexual, okay?"
    m "We're not at that level for me to be dressing like {i}that{/i} you know?"
    #if player hasnt gotten themselves locked out of nicknames like a dummy:
        m "I trust you wouldn't, you've been attentive to my feelings so far."
        m "It's why I love you~!"
        m "But it never hurts to make sure a boundary is firmly in place!"

    m "If I feel really bad about a style you try to give me, I'll let you know, okay [player]?"

if mas_isMoniUpset():
    m "Hm, a little, I suppose."
    m "It feels like another reminder that you don't see me as a real being.{fast}{nw}"
    m "It feels like another reminder that{fast} I'm trapped here."
    m "There's not much I can do about it here though."
    m "Just... Try not to turn me into your punchline with weird clothes.{cp=0.2}{nw}"
    m "Just... Try not to{fast} put me in anything odd or offensive, will you?"
    m "That's all I ask."

else:
    m "..."
    m "Does it even matter...?"
    m "..."
return