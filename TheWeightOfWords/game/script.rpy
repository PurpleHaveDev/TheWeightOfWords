# The script of the game goes in this file.
#this is the main file for this game. Any Setup for Characters or Variables pls do in seperate sheets found in rnpy folder.
#Please keep this as organized as possible

    
label start:



    if English==False:                                          #Das Deutsche Menu 
        menu:
            "Start":
                jump Game_Start

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
                    "Kühle Menschen haben an diesem Spiel gearbeitet."
                    jump start
                else:
                    "Cool people have worked on this game."
                    jump start

            "Lautstärke":
                label LautstärkeDE:                              #Lautstärke wird prozentual gerechnet, deswegen "0.0~" 
                    if English==False:
                            menu:
                                "Lauter":
                                    $Lautstärke=Lautstärke+0.05
                                    jump LautstärkeDE
                                "Leiser":
                                    $Lautstärke=Lautstärke-0.05
                                    jump LautstärkeDE
                                "Zurück":
                                    jump start                      #Muss noch nen Weg finden, dass man hier nur ein menu zurück geschickt wird/in ndem Menu bleibt
                        
                    else:
                            menu:
                                "Louder":
                                    $Lautstärke=Lautstärke+0.05
                                    jump LautstärkeDE
                                "Quieter":
                                    $Lautstärke=Lautstärke-0.05
                                    jump LautstärkeDE
                                "Back":
                                    jump start
    else: 
        menu:                                                      #Das Englische Menu
            "Start":
                jump Game_Start

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
                    "Kühle Menschen haben an diesem Spiel gearbeitet."
                    jump start
                else:
                    "Cool people have worked on this game."
                    jump start


            "Volume":
                label LautstärkeEN:                                        #Lautstärke wird prozentual gerechnet, deswegen "0.0~" 
                    if English==False:
                            menu:
                                "Lauter":
                                    $Lautstärke=Lautstärke++0.05      
                                    jump LautstärkeEN                                                       
                                "Leiser":
                                    $Lautstärke=Lautstärke--0.05    
                                    jump LautstärkeEN                      
                                "Zurück":
                                    jump start                      #Muss noch nen Weg finden, dass man hier nur ein menu zurück geschickt wird/in ndem Menu bleibt
                                
                    else:
                            menu:
                                "Louder":
                                    $Lautstärke=Lautstärke++0.05
                                    jump LautstärkeEN
                                "Quieter":
                                    $Lautstärke=Lautstärke--0.05
                                    jump LautstärkeEN
                                "Back":
                                    jump start

label Game_Start:

    if English==False:
        NA "DAS NARRATIV"
        menu:
            "Szenario1":
                $Szenario = 1
                $Aggression = 0
                $Decisions= [0,0,0,0,0,0]
                $Which_decision= 1
                jump Szenario1
            "Szenario2":
                $Szhenario = 2
                $Szenario = 1
                $Aggression = 0
                $Decisions= [0,0,0,0,0,0]
                $Which_decision= 1
                pass #jump Szenario2
            "Szenario3":
                pass #jump Szenario3

    else:
        NA "THE NARRATIVE"
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