
if English==False:
    label Szenario1:
        NW "Platzhalter Text."                                                                                   #Hier ist das setup des szenarios in Form eines Zeitzungsartikels
        NW "Platzhalter Text.."
        NW "Platzhalter Text..."
        NA "Du musst jetzt eine Rede halten."                                                                   #Anleitung zum kommenden Gameplay
        NA "Wähle Bausteine der Rede aus um deine Zuhörer in eine bestimmte Richtung zu lenken."

    label Decision:
        $Box_option_height = 600
        $Box_option_width = 600
        $Box_option_image_width = 500
        $Box_option_image_height = 500
        $Decision1 = True
 
        call screen Rede_Menu_Style


    label Decision_stage_1:
        $which_decision = which_decision+1
        $Function(renpy.notify, "Das klappt")
        while Decision1==True:
            if Decisions[0]==1:
                $Speech[0] = ["Rede1_Einstieg1"]
                $Decision1 = False 
            elif Decisions[0]==2:
                $Speech[0] = ["Rede1_Einstieg2"]
                $Decision1 = False 
            elif Decisions[0]==3:
                $Speech[0] = ["Rede1_Einstieg3"]
                $Decision1 = False 
            elif Decisions[0]==4:
                $Speech[0] = ["Rede1_Einstieg4"]
                $Decision1 = False 
            else:
                pass
        $Decision2 = True
        jump Decision

    label Decision_stage_2:
        $which_decision = which_decision+1        
        $Function(renpy.notify, "Das klappt2")
        while Decision2==True:
            if Decisions[1]==1:
                $Speech[1] = ["Rede1_Reaktion1"]
                $Decision2 = False
            elif Decisions[1]==2:
                $Speech[1] = ["Rede1_Reaktion2"]
                $Decision2 = False
            elif Decisions[1]==3:
                $Speech[1] = ["Rede1_Reaktion3"]
                $Decision2 = False
            elif Decisions[1]==4:
                $Speech[1] = ["Rede1_Reaktion4"]
                $Decision2 = False
            else:
                pass
        $Decision3 = True
        jump Decision
    
    label Decision_stage_3:
        $which_decision = which_decision+1
        $Function(renpy.notify, "Das klappt3")
        while Decision3==True:
            if Decisions[2]==1:
                $Speech[2] = ["Rede1_Hinführung1"]
                $Decision3 = False 
            elif Decisions[2]==2:
                $Speech[2] = ["Rede1_Hinführung2"]
                $Decision3 = False 
            elif Decisions[2]==3:
                $Speech[2] = ["Rede1_Hinführung3"]
                $Decision3 = False 
            elif Decisions[2]==4:
                $Speech[2] = ["Rede1_Hinführung4"]
                $Decision3 = False 
            else:
                pass
        $Decision4 = True
        jump Decision

    label Decision_stage_4:
        $which_decision = which_decision+1        
        $Function(renpy.notify, "Das klappt4")
        while Decision4==True:
            if Decisions[3]==1:
                $Speech[3] = ["Rede1_Problem1"]
                $Decision4 = False 
            elif Decisions[3]==2:
                $Speech[3] = ["Rede1_Problem2"]
                $Decision4 = False 
            elif Decisions[3]==3:
                $Speech[3] = ["Rede1_Problem3"]
                $Decision4 = False 
            elif Decisions[3]==4:
                $Speech[3] = ["Rede1_Problem4"]
                $Decision4 = False 
            else:
                pass
        $Decision5 = True
        jump Decision

    label Decision_stage_5:
        $which_decision = which_decision+1
        $Function(renpy.notify, "Das klappt5")
        while Decision5==True:
            if Decisions[4]==1:
                $Speech[4] = ["Rede1_Erkenntnis1"]
                $Decision5 = False 
            elif Decisions[4]==2:
                $Speech[4] = ["Rede1_Erkenntnis2"]
                $Decision5 = False 
            elif Decisions[4]==3:
                $Speech[4] = ["Rede1_Erkenntnis3"]
                $Decision5 = False 
            elif Decisions[4]==4:
                $Speech[4] = ["Rede1_Erkenntnis4"]
                $Decision5 = False 
            else:
                pass
        $Decision6 = True
        jump Decision

    label Decision_stage_6:
        $which_decision = which_decision+1
        $Function(renpy.notify, "Das klappt6")
        while Decision6==True:
            if Decisions[5]==1:
                $Speech[5] = ["Rede1_Aufruf1"]
                $Decision6 = False
            elif Decisions[5]==2:
                $Speech[5] = ["Rede1_Aufruf2"]
                $Decision6 = False
            elif Decisions[5]==3:
                $Speech[5] = ["Rede1_Aufruf3"]
                $Decision6 = False
            elif Decisions[5]==4:
                $Speech[5] = ["Rede1_Aufruf4"]
                $Decision6 = False
            else:
                pass
        jump Aftermath
        
                                                                    # Als nächstes muss unbedingt ein Variablen Array erstellt werden, das trackt, welche Option gewählt wurde. 
                                                                    # Fragen zu Klären: Wie viele Varianten von Auswirkungen -"Enden"- soll es geben?
                                                                    # Wie soll die immediate Reaktion der audience aussehen?
                                                                    # Wie soll dir finale form der Auswirkungen aussehen? png's, animationen, Text?
                                                                    # Wie können wir den Punkt Hass und Manipulation noch härter heimhämern?                                                               

    label Aftermath:                
        NA "Sieh nun die Auswirkungen deiner Rede auf die Sachlage."                
        NW "Platzhalter Text."
        NW "Platzhalter Text.."
        NW "Platzhalter Text..."
        $Szenario = 1
        $Szenario = 1
        $Aggression = 0
        $Decisions= [0,0,0,0,0,0] 
        $which_decision= 1
        $Speech = ["...","...","...","...","...","..."]
        jump start  


                    # Und jz das ganze nommal auf englisch


else:
    pass