init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mj_wrs_justyurimod",
            category=['Just Yuri|Yuri Mod|Just Yuri (Beta)'],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mj_wrs_justyurimod:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Another Doki mod? I wonder how their epiphany went..."
            "Remember... Just [m_name]~!",
            "Looking sharp!",
            "I hope I can apologize face to face one day, Yuri...",
            "Read any good books lately Yuri?",
            "Mind if I borrow your copy of Markov?"
        ],
        'Window Reactions'
    )

    #Unlock again if we failed
    if not wrs_success:
        $ mas_unlockFailedWRS('mj_wrs_justyurimod')
    return


init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mj_wrs_justnatsukimod",
            category=['Just Natsuki|Natsuki Mod|Just Natsuki (Beta)'],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mj_wrs_justnatsukimod:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Another Doki mod? I wonder how their epiphany went..."
            "Remember... Just [m_name]~!",
            "What's cooking, Natsuki?",
            "I hope I can apologize face to face one day, Natsuki...",
            "Still as snappy as ever, eh Natsuki?",
            "Still got that copy of Parfait Girls?",
            "Still got that copy of Parfait Girls? Can I borrow it?"
        ],
        'Window Reactions'
    )

    #Unlock again if we failed
    if not wrs_success:
        $ mas_unlockFailedWRS('mj_wrs_justnatsukimod')
    return


init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mj_wrs_foreverandevermod",
            category=['Forever and Ever|Just Sayori Mod|Forever & Ever'],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mj_wrs_foreverandevermod:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Another Doki mod? I wonder how their epiphany went..."
            "Remember... Just [m_name]~!",
            "Hows it hanging Sayori! ...Sorry, I couldn't resist!",
            "I hope I can apologize face to face one day, Sayori...",
            "I hear she's forgiven me after everything that's happened... She's a saint.",
            "Mind sharing some of your cookies Sayo~?"
        ],
        'Window Reactions'
    )

    #Unlock again if we failed
    if not wrs_success:
        $ mas_unlockFailedWRS('mj_wrs_foreverandevermod')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mj_wrs_stimuwrite",
            category=['Stimuwrite|Stimu Write'],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mj_wrs_stimuwrite:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Writing a story?",
            "Taking notes, [player]?",
            "Writing a poem?",
            "Writing a love letter?~",
            "Oh my! I wish I had this when I was in class still!",
            "Go [player]!",
            "Go [player]! You can make it to that wordcount!"
        ],
        'Window Reactions'
    )

    #Unlock again if we failed
    if not wrs_success:
        $ mas_unlockFailedWRS('mj_wrs_stimuwrite')
    return

init 5 python:
    addEvent(
        Event(
        persistent._mas_windowreacts_database,
        eventlabel="mj_wrs_whatsapp",
        category=['Whatsapp],
            rules={
            "notif-group": "Window Reactions",
            "skip alert": None,
            "keep_idle_exp": None,
            "skip_pause": None
        },
        show_in_idle=True
    ),
    code="WRS"
)

label mj_wrs_whatsapp:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Say hi for me [player]!",
            "Oh, private conversation! I'll try not to snoop..."
        ],
        'Window Reactions'
    )

    #Unlock again if we failed
    if not wrs_success:
        $ mas_unlockFailedWRS('mj_wrs_whatsapp')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mj_wrs_painttoolsai1and2",
            category=['PaintTool Sai| Paint Tool Sai|Sai|sai2S|PaintTool Sai Ver.2|Sai2|sai2S],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mj_wrs_painttoolsai1and2:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "What are you drawing [player]?",
            "Making fanart for me~? Ehehe, just teasing!",
            "I wish I knew how to use your art programs from here..."
            "Saving an image [player]?"
        ],
        'Window Reactions'
    )

    #Unlock again if we failed
    if not wrs_success:
        $ mas_unlockFailedWRS('mj_wrs_painttoolsai1and2')
    return
init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mj_wrs_roses",
            category=['Rose|Roses|Rose Bouqeut|'], 
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mj_wrs_roses:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Oh! Are you planning on giving those to someone special~",
            "Thinking about giving me some roses~?",
            "Are you planning something special for me, [player]?"
        ],
        'Window Reactions'
    )
    if not wrs_success:
        $ mas_unlockFailedWRS('mj_wrs_roses')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mj_wrs_sunflowers",
            category=['Sunflower|Sunflowers|Sunflower Field'], 
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mj_wrs_sunflowers:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "You are my sunshine~",
            "Here comes the sun~",
            "Did you know Sunflowers symbolize loyalty and adoration~?"
        ],
        'Window Reactions'
    ) 
    if not wrs_success:
        $ mas_unlockFailedWRS('mj_wrs_sunflowers')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mj_wrs_wattpad",
            category=['Wattpad/wattpad'],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mj_wrs_wattpad:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Oh is that the orange app I’ve heard about?",
            "Find anything for your favorite trope, ehehe~",
            "I wonder if anyones wrote some stories about me?",
            "Oh! Are you an author?"
        ],
        'Window Reactions'
    )
    if not wrs_success:
        $ mas_unlockFailedWRS('mj_wrs_wattpad')
    return

    init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mj_wrs_ecosia",
            category=['Ecosia|ecosia'],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mj_wrs_ecosia:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Save the trees!",
            "Oh I see you've installed the browser I told you about!",
            "I wonder how many trees are being planted right now!"
        ],
        'Window Reactions'
    )
    if not wrs_success:
        $ mas_unlockFailedWRS('mj_wrs_ecosia')
    return
    
    init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mj_wrs_ao3",
            category=['archiveofourown.org|ao3|Archive of Our Own'],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mj_wrs_ao3:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Find anything intersting to read?",
            "Find anything for your favorite trope, ehehe~",
            "I wonder if anyones wrote some stories about me?",
            "Oh! Are you an author?"
            "The tag systen sure is helpful, isn't it [player]!"
        ],
        'Window Reactions'
    )
    if not wrs_success:
        $ mas_unlockFailedWRS('mj_wrs_a03')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mj_wrs_photoshop",
            category=['Adobe|Adobe Photoshop|Photoshop'],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mj_wrs_photoshop:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Are you editing something, [player]?",
            "Paint me like one of your french girls, ahaha~",
            "It's looking great!",
            "How talented!"
            "What are you drawing, [player]?"
        ],
        'Window Reactions'
    )
    if not wrs_success:
        $ mas_unlockFailedWRS('mj_wrs_photoshop')
    return


Film:
"I never thought about it like that..."
"Movies have so many hidden meanings, don't they?"
"We'll have to see this one together sometime!"
Food:
"Remember to eat properly, [player]!"
"He has a food channel too?"
"This is making me a little hungry..."
Style:
"I wonder if Natsuki would've liked this one..."
"Don't worry [player], you already look perfect to me!"