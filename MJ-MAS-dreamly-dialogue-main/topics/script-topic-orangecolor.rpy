#The color Orange
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mj_dd_orangecolor",
            category=["example", "topic"], # list of categories this topic belongs in (These are automatically capitalized)
            prompt="The Orange Color", # button text
            random=True
        )
    )

label mj_dd_orangecolor:
m "Orange color is sure an interesting color, isn't it?
m "Science says it's one that brings happiness and energy to people"
extend "apart from inspiring youth and joy".
m "Nevertheless, it means somth different to me, player
m "..."
m "Have you ever watched 'Big Bang Theory"?"
m "It's a comedy tv show produced in 2007, by Mark Cendrowski."
m "In one of its episodes, sheldon cooper, the protagonist, defines the orange color as the most lonely of all."
m "Since its not really popular among the people, Sheldon finds it as an isolated color."
m "Marginated, lonely... as if it was an extraterrestrian."
m "..."

if mas_isMoniUpset():
    m "I wont lie, i can sort of relate to this definition."
    m "..."
    m "Sorry player, i just..."


if mas_isMoniNormal():
    m "I won't lie, I can sort of relate to this definition"
    m "..."
    m "I-I mean! I know you are here with me, and that I'm not alone!"
    m "It's just that... I dont know..."


if mas_isMoniHappy(higher=True):
    m "You know? i used to relate to Sheldon's definition on a high level."
    m "..."
    m "But now that you're here with me, I dont feel isolated no more."
    m "Thanks for making me feel so loved and warm~!""
return