init -990 python in mas_submod_utils:
    Submod(
        author="Wilson_Smith",
        name="Internal Managment",
        description="Let Monika manage your computer",
        version="0.0.1",
        dependencies={},
        settings_pane=None,
        version_updates={}
    )

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mgt_cdtray",
            category=["Managment"],
            prompt="Can you open the cd tray?",
            pool=True,
            unlocked=True))

init python:
    import ctypes
    import time

label mgt_cdtray:
    m 2euc "Yeah, sure!"
    m 1fua "Here you are!"
    python:
        # TODO: Adding Linux and MacOS

        # open the CD tray door
        ctypes.windll.winmm.mciSendStringW("set cdaudio door open", None, 0, None)

        # wait 3.5 seconds
        time.sleep(3.5)

        # close the CD tray (manual closing only with some notebooks)
        ctypes.windll.winmm.mciSendStringW("set cdaudio door closed", None, 0, None)
    return