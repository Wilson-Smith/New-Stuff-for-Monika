init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mj_dd_ecosiapleasesponserus", # /j
            category=["example", "topic"], # list of categories this topic belongs in (These are automatically capitalized)
            prompt="Ecosia", # button text
            random=True
        )
    )

label mj_dd_ecosiapleasesponserus:
    m 2eud "Hey, [player]?"
    m 7eud "Have you ever wondered if there were ways to help the environment?"
    m 7mtd "In this day and age, it can be hard to tell if your efforts to help or lower your carbon footprint actually work..."
    m 3htb "For me, I think {i}any{/i} effort is reason to be proud of, [mas_get_player_nickname()]." #check if that var is right
    m 1fta "And as technology spreads people make more ways to help from the comfort of your home."
    extend " One of them is Ecosia!"
    m 3wtb "Ecosia is a search engine that allows you to plant trees while you search things online."
    m 4wub "It donates the money you generate from your searches to the Ecosia organisation, which fully utilises it for tree planting."
    m 6sub "It also has browser extensions, so you can integrate it more seamlessly into your browsing uses!"
    m 4hua "You can learn about it more here!" #insert link to ecosia site
    m 4hua {a=https://www.ecosia.org/[Ecosia]}{i}{u}[Ecosia]{/u}{/i}{/a}
    m 6fua "..."
    m 2husdlb "I'm not sponsored by Ecosia, by the way-{w=0.3}{nw}"
    extend "Ehehe..." #(Face like: 😅)
    m 7wub "It's just a very interesting way to be ecological in your daily life!"
    m 2dkd "Sometimes I get worried about what the state of your reality might be when I finally can join it."
    m 7kub "So if I can help in anyway to make your reality a better place, I will."
    m 1hub "So thanks for listening, [player]! Let's make your world better together~"
    return