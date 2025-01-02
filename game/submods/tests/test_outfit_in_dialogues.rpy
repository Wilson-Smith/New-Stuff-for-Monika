init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="DDDDDD",
            category=["Us"],
            prompt="AAAAAAAAAAAAA",
            pool=True,
            unlocked=True,
            aff_range=(mas_aff.HAPPY, None),
        ),
    )

label DDDDDD:
    m 2dua "Hold on a moment..."

    call mas_transition_to_emptydesk

    pause 2
    python:

        # open the file
        f = open(renpy.loader.transfn("outfits/Reading.json"),"r")
        # iterate over its lines and do something with them
        # when finished, close the file
        sel_outfit_name = json.load(f)
        f.close()

        sel_outfit = kventis_outfit_submod.outfits[Reading]
        new_clothes = mas_sprites.CLOTH_MAP.get(sel_outfit.get("clothes"), None)
        new_hair = mas_sprites.HAIR_MAP.get(sel_outfit.get("hair"), None)
        new_acs = monika_chr.acs[2]
        missing_acs = False

        for item in sel_outfit.get("acs", []):
            new_item = mas_sprites.ACS_MAP.get(item, None)
            if new_item != None:
                new_acs.append(new_item)
            else:
                missing_acs = True
    m 1eua "Kanto"
    return

