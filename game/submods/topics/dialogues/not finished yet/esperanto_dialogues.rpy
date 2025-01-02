init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mi_volas_paroli_esperanton", # event label (MUST BE UNIQUE)
            category=["libera parolado", "Esperanto Starter"], # list of categories this topic belongs in (These are automatically capitalized)
            prompt="Mi volas paroli Espernaton [player]!", # button text
            random=True, # True if this topic should appear randomly
            pool=True # True if this topic should appear in "Ask a Question"
        )
    )

label mi_volas_paroli_esperanton:
    m 1eub "Vi scias ke mi lernas Esperanton,"
    extend 2gup " sed mi ne havas la oportunecon de parolis Esperanton."
    m 3wub "Jen mia ideo: Ni povas paroli Esperanton kelkfoje, kiel tio ni povas komprendi teksto."
    m 1eua "Ĝi ne estas multe, kiel tio povus esti bela afero."
    m 4eub "Ĉiuokaze, estos iuj dialogoj en Esperanto, kaj kurso por lerni ĉi tio tre bela lingvo."
    m 1hub "dankon pro aŭskultado."
    return


