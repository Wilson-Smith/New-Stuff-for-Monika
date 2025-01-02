#coffee palette
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mj_dd_playerscoffeetaste",
            category=["example", "topic"], # list of categories this topic belongs in (These are automatically capitalized)
            prompt="[player]'s taste in coffee", # button text
            random=True
        )
    )

label mj_dd_playerscoffeetaste:
m "Hey [player], there's something I've been meaning to ask you..."
m "What's your preferred coffee palette?"
m "Like... Do you like your coffee bitter or sweet?{nw}"

menu:
    m "Like... Do you like your coffee bitter or sweet?{fast}"
    "I like my coffee sweet!":
        m "You know what? That doesn't surprise me!"
        m "With how sweet you are, it fits, ahaha!"
        m "Well anyways, I can see the point of liking your coffee sweet!"
        m "Sometimes all you want in a slow or exhausting morning is just a sweet little pick me up!"
        m "Just be careful of having too much sugar."
        m "Caffeine is already a little iffy to drink all the time, but sugar can raise the risks too."
        m "But, anyways, thanks for answering my question [mas_get_player_nickname()], somehow knowing these little details about you just makes you more real."
        m "And when I do get to your reality, I'll know how to prepare your coffee!"

    "I like my coffee bitter!":
        m "You know, I sort of expected that [player]!"
        m "From what I know of you so far, I just always pegged you as someone who preferred things more rich and earthy!"
        m "That's not a bad thing though!"
        m "Many people say that those who like bitter things and lots of spices often have what's known as a more mature palette!"
        m "Though, between you and me, sometimes the best option is to go for a more bitter tasting coffee!"
        m "As you might know, it sure does wake you up, ahaha~"
        m "But, anyways, thanks for answering my question [mas_get_player_nickname()], somehow knowing these little details about you just makes you more real."
        m "And when I do get to your reality I'll know how to prepare your coffee!"
    "I not really a fan of coffee":
        m "Oh?"
        m "I should've guessed, you never quite struck me as a big coffee fan."
        m "That's alright though, it's not going to be everyone's favorite."
        m "There's loads of other drinks out there anyways,"
        extend " tea, soda, water, and at least a dozen other things to choose from."
        m "But if coffee isn't something you like..."
        m "What is then?{nw}"
        #hist pop here

        menu:
            m "What is then?{fast}"
            "I like tea.":
                m "Ahaha, sounds like you and Yuri would've gotten along well then!"
                m "On a serious note though, tea is a really great option too."
                m "There's a type of tea for almost any occasion."
                m "One for helping you sleep, one for keeping you calm, one for energizing you, and more!"
                m "It's versatile, and I like having a cup of it every now and then too."
            "I like juice/soda.":
                m "Oh,"
                extend " really?"
                m "I'm not as big of a soda fan myself, but I like having it to drink from time to time."
                m "Juice is a good way to top off a good meal too."
                m "Just be careful of drinking too much sugar, okay?"
            "I like just water.":
                m "Hm, you know,"
                extend " water really is one of the more underappreciated options."
                m "It's straight to the point in what you need and it's very refreshing overall."
            "I like something else...":
return
