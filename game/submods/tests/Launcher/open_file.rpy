init -990 python in mas_submod_utils:
    Submod(
        author="Wilson_Smith (not distribuibile)",
        name="File Launcher",
        description="Let Monika open your file",
        version="0.0.1",
        dependencies={},
        settings_pane=None,
        version_updates={}
    )

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_openfile",
            category=['Launcher'],
            prompt="Can you please open a file?",
            action=EV_ACT_PUSH,
            random=False,
            pool=True,
            unlocked=True
        )
    )

init python:
    import webbrowser
    import os

label monika_openfile:
    m 1wua "Want me to open a file?"
    m 4wub "Let me open it for you!"
    jump Moni_fileselection
    return

label Moni_fileselection:
    m 1wua "What do you prefer?"
    $ _history_list.pop()
    menu:
        "Spotify":
            jump Moni_spotify
        "Cyberpunk 2077":
            jump Moni_cyberpunk2077
        "Opera GX":
            jump Moni_operagx
        "Visual Studio Code":
            jump Moni_vscode
        "It's another app":
            jump Moni_custom

label Moni_spotify:
    m 2hub "There we go!"
    python:
        webbrowser.open_new('C:\Users\utente\AppData\Roaming\Spotify\Spotify.exe')
    return

label Moni_cyberpunk2077:
    m 2hub "There we go!"
    python:
        #webbrowser.open_new('"C:\Users\utente\Desktop\Monika After Story\output\hard_disk_opener.exe"')
        webbrowser.open_new('"D:\\Games\\Cyberpunk 2077\\bin\\x64\\Cyberpunk2077.exe"')
        webbrowser.open_new('"C:\Users\utente\Desktop\cpah-1.1.4.exe-955-1-1-4-1621649428.exe"')
    return

label Moni_operagx:
    m 2hub "There we go!"
    python:
        webbrowser.open_new('"C:\Users\utente\AppData\Local\Programs\Opera GX\launcher.exe"')
    return

label Moni_vscode:
    m 2hub "There we go!"
    python:
        webbrowser.open_new('"C:\Program Files\Microsoft VS Code\Code.exe"')
    return

label Moni_custom:
    python:
        import os
        makegift = mas_input(_("Write the entire path (Including .exe/.png...)"),
                            allow=" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_\/ *+.0123456789",
                            screen_kwargs={"use_return_button": True, "return_button_value": "nevermind"})
    if makegift == "nevermind":
        return
    else:
        m 1sub "there you go"
        $ webbrowser.open_new(makegift)
    return