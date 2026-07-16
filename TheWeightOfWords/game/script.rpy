# The script of the game goes in this file.
#this is the main file for this game. Any Setup for Characters or Variables pls do in seperate sheets found in rnpy folder.
#Please keep this as organized as possible

    
label start:



    if English==False:  
        call screen mainmenu                                        #Das Deutsche Menu 

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
                    "Kuehle Menschen haben an diesem Spiel gearbeitet."
                    jump start
                else:
                    "Cool people have worked on this game."
                    jump start


            "Volume":
                label LautstaerkeEN:                                        #Lautstaerke wird prozentual gerechnet, deswegen "0.0~" 
                    if English==False:
                            menu:
                                "Lauter":
                                    $Lautstaerke=Lautstaerke++0.05      
                                    jump LautstaerkeEN                                                       
                                "Leiser":
                                    $Lautstaerke=Lautstaerke--0.05    
                                    jump LautstaerkeEN                      
                                "Zurueck":
                                    jump start                      #Muss noch nen Weg finden, dass man hier nur ein menu zurueck geschickt wird/in ndem Menu bleibt
                                
                    else:
                            menu:
                                "Louder":
                                    $Lautstaerke=Lautstaerke++0.05
                                    jump LautstaerkeEN
                                "Quieter":
                                    $Lautstaerke=Lautstaerke--0.05
                                    jump LautstaerkeEN
                                "Back":
                                    jump start

label Game_Start:

    if English==False:
        NA "DAS NARRATIV"
        call screen Szenarios

    else:
        NA "THE NARRATIVE"
        menu:
            "Scenario1":
                $Szenario = 1
                jump Szenario1
            "Scenario2":
                $Szenario = 2
                pass #jump Szenario2
            "Scenario3":
                $Szenario = 3
                pass #jump Szenario3

            
return