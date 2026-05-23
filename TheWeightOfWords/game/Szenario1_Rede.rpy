
if English==False:
    label Szenario1:
        NW "Platzhalter Text."                                                                                   #Hier ist das setup des szenarios in Form eines Zeitzungsartikels
        NW "Platzhalter Text.."
        NW "Platzhalter Text..."
        NA "Du musst jetzt eine Rede halten."                                                                   #Anleitung zum kommenden Gameplay
        NA "Wähle Bausteine der Rede aus um deine Zuhörer in eine bestimmte Richtung zu lenken."

    label decision:
        $Box_option_height = 600
        $Box_option_width = 600
        $Box_option_image_width = 500
        $Box_option_image_height = 500
 
        call screen Rede_Menu_Style


    label Decision_stage_1:
        $which_decision = which_decision+1
        $Function(renpy.notify, "Das klappt")
        jump decision

    label Decision_stage_2:
        $which_decision = which_decision+1
        jump decision
    
    label Decision_stage_3:
        $which_decision = which_decision+1
        jump decision
                                                                # Als nächstes muss unbedingt ein Variablen Array erstellt werden, das trackt, welche Option gewählt wurde. 
                                                                    # Fragen zu Klären: Wie viele Varianten von Auswirkungen -"Enden"- soll es geben?
                                                                    # Wie soll die immediate Reaktion der audience aussehen?
                                                                    # Wie soll dir finale form der Auswirkungen aussehen? png's, animationen, Text?
                                                                    # Wie können wir den Punkt Hass und Manipulation noch härter heimhämern?                                                               
                    
    NA "Sieh nun die Auswirkungen deiner Rede auf die Sachlage."                
    NW "Platzhalter Text."
    NW "Platzhalter Text.."
    NW "Platzhalter Text..."
    jump start  


                    # Und jz das ganze nommal auf englisch


else:
    pass