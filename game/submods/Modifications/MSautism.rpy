default persistent._mas_pm_is_autistic = None

#init -810 python:
#    store.mas_history.addMHS(MASHistorySaver(
#        "monika_autism_pm",
#        datetime.datetime(2019, 1, 1),
#        {
#            "_mas_pm_is_autistic"
#        },
#        use_year_before=True,
#        dont_reset=True
#    ))

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_autism",category=["you","life"],prompt="Autism",random=True))

label monika_autism:
    m 3eud "Hey [player], do you know what autism is?"
    $_history_list.pop()
    menu:
        "Yes, I do.":
            m 1eub "Oh, that's great!"
            m 1esb "How do you know about it?"
            $_history_list.pop()
            menu:
                "I'm autistic!":
                    m 3wub "Oh, thank you for telling me!"
                    m 3ekd "I know a lot of people think that autism is something bad, but I'm glad I won't have to explain that to you."
                    m 3rkd "You probably have to deal with those stereotypes..."
                    m 7eka "Thank you for sharing that, [player]."
                    m 7esa "Just know, if you're ever having a bad day or want to talk about your special interests-"
                    m 5hsb "I'll always be happy to listen!"
                    $ persistent._mas_pm_is_autistic = True

                "I know someone who's autistic.":
                    m 1eub "Oh, that's nice!"
                    m 1ekc "I was sad to learn that autistic people are so often mistreated."
                    m 2fua "I know you're nothing but kind to your freinds and family though, [mas_get_player_nickname()]."
                    m 4esd "Remember to always listen to what autistic people say, as they're often spoken over."
                    m 4sub "Thanks for listening to me talk, [player]!"

                "I've heard about it.":
                    m 1eub "Oh, alright!"
                    m 1ekc "I was sad to learn that autistic people are so often mistreated."
                    m 2fua "I know you're nothing but kind to people though, [mas_get_player_nickname()]."
                    m 4esd "Remember to always listen to what autistic people say, as they're often spoken over."
                    m 4sub "Thanks for listening to me talk, [player]!"

                "I've done some research on it.":
                    m 1eub "Oh, that's great!"
                    m 1ekc "I was sad to learn that autistic people are so often mistreated."
                    m 2fua "I know you're nothing but kind to people though, [mas_get_player_nickname()]."
                    m 4esd "Remember to always listen to what autistic people say, as they're often spoken over."
                    m 4sub "Thanks for listening to me talk, [player]!"

        "No, I don't.":
            m 3ekb "Well, that's alright [player]"
            m 3rkd "It's been misrepresented a lot in the media."
            m 1esd "Do you want me to tell you about autism?"
            $_history_list.pop()
            menu:
                "Yes, please.":
                    m 1esb "Alright!"
                    m 4esd "Autism is a neurodevelopmental disorder."
                    m 4esd "Autistic people usually have issues with social interactions, physical touch, and eye contact."
                    m 3eua "They really enjoy what they put their mind to, though."
                    m 3wub "They're known to be pretty smart people."
                    m 2lkc "However..."
                    m 2lkd "A lot of people demonize autism, and make it seem like something awful."
                    m 2eko "But, that's just not true at all!"
                    m 1eka "I trust you not to think about people like that."
                    m 1eua "I hope you enjoyed learning about this, [player]."

                "No, thank you.":
                    m 2eka "Alright. Just let me know if you change your mind, okay?."
return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_autismspeaks",category=['society'],prompt="Autism Speaks",random=True))

label monika_autismspeaks:
    m 2esd "Hey [player], have you heard of Autism Speaks?"
    m 4efd "It's a truly terrible company."
    m 2ekd "Using the autistic comunnity as a mean of personal gains. Completely going against what they say they stand for."
    m 2efx "It's really despicable."
    m 2rusdrd "Ah, I guess I got too caught up. I haven't even told you what they do yet."
    m 2dsd "Autism Speaks is a company that sees autism as something horrible, labelling it a disease. They fund reasearch looking for some kind of 'cure'."
    m 2dfd "Their logo is a puzzle piece, symbolizing that autistic people aren't whole."
    m 2efd "They've also been known to spend less funding on their research than other autistm organizations."
    m 2dfc "..."
    m 2dkc "..."
    m 2mkd "I just don't get how some people can be so cruel."
    m 2eksdrb "I'm sorry, [player]. I didn't mean to bring down the mood."
    m 3eub "You know, there are some things you can do to support to autistic community!"
    m 3eua "You can donate to the Autistic Self Advocacy Network, run by and for autistic people!"
    m 3eua "There's also RedInstead, a movement directly apposing Autism Speaks' LightItUpBlue."
    m 1ekb "Thank you for listening to me talk about this, [player]. I hope you learned something from this."
return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_aspergers",category=['society','life'],prompt="Asperger Syndrome",random=True))

label monika_aspergers:
    m 3eua "Hey [player], do you know what Asperger syndrome is?"
    m 3eud "It's also just called Asperger's."
    m 3eud "It's a now outdated term for ASD- Autism Spectrum Disorder. It's outdated for many reasons."
    m 3ekx "For one, it was named after a Nazi physician. You can probably tell why autistic people don't want do be associated with that."
    m 3esd "Also, the autistic community has dismissed the 'functioning labels' that Asperger's was categorised into."
return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_functioninglabels",category=['society'],prompt="Functioning labels",random=True))

label monika_functioninglabels:
    m 1eud "Have you heard about functioning labels, [player]?"
    m 3eud "It's a way people categorise the 'severity' of autism."
    m 3eud "The autistic community have discarded these labels, as autism is a wide and diverse spectrum."
    m 3ekc "Some people use functioning labels to further discriminate against autistic people."
    m 3eua "Luckily, not many people use the labels anymore."
    m 3hua "So remember, if someone tries to say someone's 'high-functioning' or 'low-functioning', try to correct them! If you can't, then just dont let it change your view on autistic folks."
return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_personfirst",category=['society'],prompt="Person first language",random=True))

label monika_personfirst:
    m 2eud "Do you know what 'person-first language' is, [player]?"
    m 3eud "It's something people use because they feel like they have to remind others that autistic people are, in fact, people."
    m 2eud "A lot of autistc people refer to themselves as just that- 'autistic people'."
    m 4eud "But people who use person-first language would call them 'people with autism'."
    m 2esd "Not only is that a bit longer, it's also just unecessary."
    m 2esc "It insinuates that autism is seperate from the person, some autistic people have agreed it sounds like they're saying the autism can be removed."
    m 2eka "So please, just refer to them as 'autistic people'."
return