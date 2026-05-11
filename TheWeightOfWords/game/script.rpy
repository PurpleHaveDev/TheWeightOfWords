# The script of the game goes in this file.
#this is the main file for this game. Any Setup for Characters or Variables pls do in seperate sheets found in rnpy folder.
#Please keep this as organized as possible

label start:

    menu:
        "Start":
            jump Game_Start
            pass
        "Sprache":
            "Wähle eine Sprache"
            menu:
                "Deutsch":
                    $English=False
                    jump start
                "English":
                    $English=True
                    jump start

        "Credits":
            if English==False:
                "Projektleitung: Vora Narga"
                "Idee: Aron Agrav"
                "Autorin: Das Nörchen"
                "2D Graphiken: Miriam Löffel"
                "Programmierung: Philipp Lüer"
                jump start
            else:
                "Project Lead: Vora Narga"
                "Idea: Aron Agrav"
                "Lead Writing: Das Nörchen"
                "2D Asstes: Miriam Löffel"
                "Programming: Flip Tür"
                jump start

        "Lautstärke":
            label .VolumeSttings:
                if English==False:
                    menu:
                        "Lauter":
                            $Lautstärke=Lautstärke++0.05
                            return
                        "Leiser":
                            $Lautstärke=Lautstärke--0.05
                            return
                        "Zurück":
                            jump .VolumeSttings
                else:
                    menu:
                        "Louder":
                            $Lautstärke=Lautstärke++0.05
                            return
                        "Quieter":
                            $Lautstärke=Lautstärke--0.05
                            return
                        "Back":
                            jump .VolumeSttings


label Game_Start:
    if English==False:
        C "Das ist auf Deutsch."

    else:
        C "This is in English."

return