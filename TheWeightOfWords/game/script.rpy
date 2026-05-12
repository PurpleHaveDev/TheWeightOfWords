# The script of the game goes in this file.
#this is the main file for this game. Any Setup for Characters or Variables pls do in seperate sheets found in rnpy folder.
#Please keep this as organized as possible

label start:


    if English==False:                                          #Das Deutsche Menu 
        menu:
            "Start":
                pass

            "Sprache":
                "Wähle eine Sprache"
                menu:
                    "Deutsch":
                        $English=False
                        jump start
                    "Englisch":
                        $English=True
                        jump start

            "Entwickler":
                if English==False:
                    "Projektleitung: Nora varga"
                    "Idee: Nora Varga"
                    "Autorin: Nora Varga"
                    "2D Graphiken: Miriam Löffler"
                    "Programmierung: Philipp Lüer"
                    "Übersetzung: Nora Varga & Philipp Lüer"
                    jump start
                else:
                    "Project Lead: Nora Varga"
                    "Idea: Nora Varga"
                    "Lead Writing: Nora Varga"
                    "2D Asstes: Miriam Löffler"
                    "Programming: Philipp Lüer"
                    "Localization: Nora Varga & Philipp Lüer"
                    jump start

            "Lautstärke":                                        #Lautstärke wird prozentual gerechnet, deswegen "0.0~" 
                    if English==False:
                        menu:
                            "Lauter":
                                $Lautstärke=Lautstärke++0.05
                                return                          #Muss noch nen Weg finden, dass man hier nur ein menu zurück geschickt wird/in ndem Menu bleibt
                            "Leiser":
                                $Lautstärke=Lautstärke--0.05
                                return
                            "Zurück":
                                pass
                    else:
                        menu:
                            "Louder":
                                $Lautstärke=Lautstärke++0.05
                                return
                            "Quieter":
                                $Lautstärke=Lautstärke--0.05
                                return
                            "Back":
                                pass
    else:                                                       #Das Englische Menu
        "Start":
            pass

        "Language":
            "Choose a Language"
            menu:
                "German":
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
                    if English==False:
                        menu:
                            "Lauter":
                                $Lautstärke=Lautstärke++0.05
                                return
                            "Leiser":
                                $Lautstärke=Lautstärke--0.05
                                return
                            "Zurück":
                                pass
                    else:
                        menu:
                            "Louder":
                                $Lautstärke=Lautstärke++0.05
                                return
                            "Quieter":
                                $Lautstärke=Lautstärke--0.05
                                return
                            "Back":
                                pass


label Game_Start:
    if English==False:
        NA "Das ist auf Deutsch."
        menu:
            "Szenario1":
                $Szenario = 1
                jump Szenario1
            "Szenario2":
                $Szhenario = 2
                pass #jump Szenario2
            "Szenario3":
                $Szenario = 3
                pass #jump Szenario3

    else:
        NA "This is in English."
        menu:
            "Scenario1":
                $Szenario = 1
                jump Szenario1
            "Scenario2":
                $Szhenario = 2
                pass #jump Szenario2
            "Scenario3":
                $Szenario = 3
                pass #jump Szenario3

            
return