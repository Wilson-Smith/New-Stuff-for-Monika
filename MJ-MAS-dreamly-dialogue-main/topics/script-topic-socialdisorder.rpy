#Social Disorder  
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mj_dd_social_disorder",
            category=["example", "topic"], # list of categories this topic belongs in (These are automatically capitalized)
            prompt="Social Disorders", # button text
            random=True
        )
    )

label mj_dd_social_disorder:
    m "[Player], have you heard of the social disorder?"
    m "From what I've read, it's one of the examples of sociology."
    m "The social disorder an example of sociology is, a discorder that some people may have."
    m "It's quite common.."
    m "When disorders and immoral events occur in our society, it's called the social disorder."
    m "From the beginning of the world's existance there has always been bad things which can be attributed to corrupting human behavior.."
    m "Societies, countries, cities, communities, and families can all expreience this in several different ways."
    m "This can be from anything, [Player]."
    m "Like peer pressure and more."
    m "And I bought this topic because not only is it important to me in a way, but I also wanted to know your thoughts on it."
    m "Disorders are hard to talk about and since they're part of sociology, it makes it more difficult."
    m "If you're having problems, talk to me or someone and we can cheer you up."
return