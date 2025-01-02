## moni asking player what kind of pet would they want/if at all
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mj_dd_pets",
            category=["example", "topic"], # list of categories this topic belongs in (These are automatically capitalized)
            prompt="Player's preferences in pets", # button text
            random=True
        )
    )

label mj_dd_pets:
m "Hey, [player], do you have any pets?"
m "I wonder what kind of animals you'd take care of. I bet you'd be great at it!~"
m "So.. do you have any pets?"
menu:
     ##YES, DOG(S)
        m "Oh, really?"
        m "That makes sense, actually!"
        m "You do kind of seem like a puppy, always coming to check on me, ahaha!~"
        m "Do you have just one, or multiple?"
        m "I know that dogs are pretty social creatures, so they probably work best with a friend or two."
        m "Did you know that some dog breeds have such good sense of smell that they can sniff out medical problems?"
        m "They're called <i>bio-detection dogs</i>, and they can smell cancer! In fact, in 2006, scientists trained dogs to detect cancer from peoples breath."
        m "Other examples include dogs that can smell a general sense of someone's bloodsugar, for example, a type one diabetic could have a severely low bloodsugar without realizing it, or be unable to ask for help, and their dog could alert someone for help, or alert their owner that they need to go get something to raise their bloodsugar!"
        m "Isn't that amazing? Dogs can do so many amazing things!"
        m "Not to mention the many wonderful dogs that are more mainstream and popular nowadays, like seeing eye dogs for blind people, or the wonderfully friendly yet loyal and helpful therapy dogs!"
        m "Oh, I almost forgot to mention dogs that help search and rescue teams find people lost in rubble after disasters like tornadoes, avalanches, and other things."
        m "Oh, sorry, I got distracted, ahaha.."
        m "When I cross over, I hope I could meet them! Hopefully they like me, hehe.."
        return
    ## YES, CAT(S)
        m "Oh, really?"
        m "You know, that makes sense."
        m "You do kind of remind me of a playful kitten, sometimes. You bring me gifts all the time, just like a cat after exploring outside, ahaha!"
        m "Although, from what I've heard, cats gifts are usually not so nice.."
        m "Is it true that their back goes up a little bit if you scratch them near their tail just right?"
        m "Ahaha, sorry! That was random, I've just heard that it's a common thing with happy kitties."
        m "As far as I know, cats are usually fine on their own, but I'm sure they wouldn't mind a friend or two."
        m "Do you have multiple cats, [player]?"
        m "Either way, I'm sure your little friend loves you a lot!"
        m "I know I do!~"
        m "I wonder if they'll like me, when I cross over?"
        m "It would be nice to pet a fluffy cat. I heard their fur is <i>super</i> soft if you've got the right breed."
        return
    ## YES, REPTILE(S)
        m "Ooh, a reptile, like a lizard or a snake?"
        m "You know, that makes sense, now that I think about it."
        m "You kind of remind me of a nice little lizard enjoying the sunshine, closing its eyes and being still as its owner gives it a nice pet or two, ahaha!"
        m "Ah, sorry, that was probably weirdly specific.."
        m "Anyway, what's your reptile like?"
        m "I hear that reptiles, at least the more common ones like snakes and reptiles, enjoy more alone time, right?"
        m "I don't think they'd mind a little playdate every now and then with a friend if it's the right reptile, though."
        m "Oh, I'm getting sidetracked."
        m "What's your reptile like? Do you have multiple, or just the one?"
        m "It'd be really cool to pet a lizard, or a snake when I cross over!"
        m "Ahaha, hopefully they like me.. that would be pretty awkward if they didn't."
        return
    ## YES, AQUATIC ANIMAL(S)
        m "Oh, really?"
        m "You know, now that I think about it, you do kind of remind me of a turtle. Cold and quiet but warm and loving, ahaha!~"
        m "I hear aquatic animals usually need friends so they aren't lonely, right?"
        m "I wonder what your water-loving friends are like?"
        m "Ooh, feeding fishes with you would be nice when I cross over."
        m "And if it's not a fish, I'm sure they'd still be really fun to hang around with!"
        m "Hopefully they like me, haha.."
        return
    ## YES, RODENT(S)
        m "Wow, really?"
        m "Rodents are actually really cute once you get to know them!"
        m "I wish more people weren't so assuming of rats and mice and such. They're actually very clean and kind!"
        m "Do you have rats.. or maybe mice?"
        m "Oh! Maybe you have a hamster or a gerbil instead?"
        m "Maybe something like a chinchilla or a guinea pig?"
        m "Ahh, all of those sound adorable and nice to hang out with!"
        m "I hear rodents are social and always in need of a friend or two, right?"
        m "I hope your little friends are nice to each other!"
        m "It would be really fun to make a little obstacle course for those smart little cuties one day when I cross over."
        return
    ## YES, FARM ANIMAL(S)
        m "Ooh, really?"
        m "Do you perhaps live on a farm, [player]?"
        m "I hear farm animals are fairly social creatures. I wonder if you've got a friend or two for them?"
        m "There are so many different kinds of farm animals!"
        m "Maybe you've got some cows or pigs?"
        m "Ooh, maybe a horse?"
        m "Ah! I can't forget about chickens!"
        m "I wonder what farm animals you've got?"
        m "It would be fun to ride a horse with you one day, [player]."
        return
    ## YES, BIRD(S)
        m "Oh, really?"
        m "What kind of birds? Maybe a Quetzal?~"
        m "Ooh, maybe a parrot or a cockatiel?"
        m "Quetzals will forver be my favorite, though! They're so majestic, and their song is nice, too."
        m "I could go on forever with Quetzals!"
        m "Did you know that the Mayans made a stone pyramid that, when you clapped, the echo would return as a Quetzal's song?"
        m "That's just amazing! I didn't know engineering could be so wonderful."
        m "Ah, I'm getting all sidetracked! Sorry, ahaha.."
        m "I hope we could take care of your bird together one day, [player]."
        return
    ## YES, OTHER(S)
        m "Oh, really?"
        m "Hm.. I thought I covered a lot of animals with everything else I put on those options."
        m "Oh well, you can never cover every animal ever, ahaha!~"
        m "I'd love to know all about them, [player]!"
        m "Do you have multiple, or just one?"
        m "It would be nice to take care of them together, whenever I cross over."
        m "For now, you can just tell me all about them!~"
        return
    ## NO, AND I DON'T WANT ANY
        m "Oh, okay."
        m "That makes sense! Not everyone has the time and energy to care for something that's entirely dependent on them."
        m "Of course, not wanting one just because, is fine too!"
        m "It would be nice to settle down with you after a long day of work, have a nice little dinner and then lay down on the couch, maybe fall asleep after watching a movie."
        m "Maybe we could get one together in the future, if you'd like?"
        return
    ## NO, BUT I WANT ONE
        m "Oh, really?"
        m "Are you looking at options for pets currently, or are you just thinking about it?"
        m "Remember to always go to shelters!"
        m "The animals there are healthier, and you can give a wonderful pet that wasn't treated fairly a nice home."
        m "I wonder if whenever I cross over, you may have one then?"
        m "Whatever option you choose, I'll be supporting you all the way!"
        return
    ## NO, I'M NOT ABLE TO TAKE CARE OF ANY
        m "Oh.. really?"
        m "I'm sorry, [player]. I can stop talking about this, if you want."
        m "I can kind of relate to it, though, being in here.."
        m "I would love a Quetzal to take care of, but I'd feel bad trapping it in here."
        m "Maybe when I cross over, we can take care of it together?"
        m "I can do the things you don't have the energy for, like taking them on walks, or cleaning a litterbox, and you can feed them. We could play with them together."
        m "That sounds nice."
        return