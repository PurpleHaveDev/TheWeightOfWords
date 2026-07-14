
label Szenario1:
    if English==False:  
        $Zeitungshöhe=0
        $Handyhöhe=0
        $Aktenhöhe=0
        $which_decision=1
        call screen Scenario1_Intro                                                                        #Hier ist das setup des szenarios in Form eines Zeitzungsartikels
        NW "(hier wäre jetzt ein Bild von der Zeitung, die den Anschlag beschreibt)"
        NW "539 Tote bei Anschlag auf die Hauptstadt. Bevölkerung in Schockstarre. Regierung unter Druck."


        label Tutorial:
            NA "Du musst jetzt eine Rede halten."                                                                   #Anleitung zum kommenden Gameplay
            NA "Wähle Bausteine der Rede aus um deine Zuhörer in eine bestimmte Richtung zu lenken."

        label Decision:
            $Box_option_height = 600
            $Box_option_width = 600
            $Box_option_image_width = 900
            $Box_option_image_height = 500
            $Decision1 = True
    
            call screen Rede_Menu_Style


        label Decision_stage_1:
            $which_decision = which_decision+1
            $Function(renpy.notify, "Das klappt")
            while Decision1==True:
                if Decisions[0]==1:
                    $Speech[0] = Rede1_Einstieg1
                    $Auswirkung[0] = "+1"
                    $Decision1 = False 
                elif Decisions[0]==2:
                    $Speech[0] = Rede1_Einstieg2
                    $Auswirkung[0] = "+2"
                    $Decision1 = False                 
                elif Decisions[0]==3:
                    $Speech[0] = Rede1_Einstieg3
                    $Auswirkung[0] = "-1"
                    $Decision1 = False 
                elif Decisions[0]==4:
                    $Speech[0] = Rede1_Einstieg4
                    $Auswirkung[0] = "-2"
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
                    $Speech[1] = Rede1_Reaktion1
                    $Auswirkung[1] = "+1"
                    $Decision2 = False
                elif Decisions[1]==2:
                    $Speech[1] = Rede1_Reaktion2
                    $Auswirkung[1] = "+2"
                    $Decision2 = False
                elif Decisions[1]==3:
                    $Speech[1] = Rede1_Reaktion3
                    $Auswirkung[1] = "-1"
                    $Decision2 = False
                elif Decisions[1]==4:
                    $Speech[1] = Rede1_Reaktion4
                    $Auswirkung[1] = "-2"
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
                    $Speech[2] = Rede1_Hinfuehrung1
                    $Auswirkung[2] = "+1"
                    $Decision3 = False 
                elif Decisions[2]==2:
                    $Speech[2] = Rede1_Hinfuehrung2
                    $Auswirkung[2] = "+2"
                    $Decision3 = False 
                elif Decisions[2]==3:
                    $Speech[2] = Rede1_Hinfuehrung3
                    $Auswirkung[2] = "-1"
                    $Decision3 = False 
                elif Decisions[2]==4:
                    $Speech[2] = Rede1_Hinfuehrung4
                    $Auswirkung[2] = "-2"
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
                    $Speech[3] = Rede1_Problem1
                    $Auswirkung[3] = "+1"
                    $Decision4 = False 
                elif Decisions[3]==2:
                    $Speech[3] = Rede1_Problem2
                    $Auswirkung[3] = "+2"
                    $Decision4 = False 
                elif Decisions[3]==3:
                    $Speech[3] = Rede1_Problem3
                    $Auswirkung[3] = "-1"
                    $Decision4 = False
                elif Decisions[3]==4:
                    $Speech[3] = Rede1_Problem4
                    $Auswirkung[3] = "-2"
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
                    $Speech[4] = Rede1_Erkenntnis1
                    $Auswirkung[4] = "+1"
                    $Decision5 = False 
                elif Decisions[4]==2:
                    $Speech[4] = Rede1_Erkenntnis2
                    $Auswirkung[4] = "+2"
                    $Decision5 = False 
                elif Decisions[4]==3:
                    $Speech[4] = Rede1_Erkenntnis3
                    $Auswirkung[4] = "-1"
                    $Decision5 = False 
                elif Decisions[4]==4:
                    $Speech[4] = Rede1_Erkenntnis4
                    $Auswirkung[4] = "-2"
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
                    $Speech[5] = Rede1_Aufruf1
                    $Auswirkung[5] = "+1"
                    $Decision6 = False
                elif Decisions[5]==2:
                    $Speech[5] = Rede1_Aufruf2
                    $Auswirkung[5] = "+2"
                    $Decision6 = False
                elif Decisions[5]==3:
                    $Speech[5] = Rede1_Aufruf3
                    $Auswirkung[5] = "-1"
                    $Decision6 = False
                elif Decisions[5]==4:
                    $Speech[5] = Rede1_Aufruf4
                    $Auswirkung[5] = "-2"
                    $Decision6 = False

                else:
                    pass
            jump Decision

                                                                        # Als nächstes muss unbedingt ein Variablen Array erstellt werden, das trackt, welche Option gewählt wurde. 
                                                                        # Fragen zu Klären: Wie viele Varianten von Auswirkungen -"Enden"- soll es geben?
                                                                        # Wie soll die immediate Reaktion der audience aussehen?
                                                                        # Wie soll dir finale form der Auswirkungen aussehen? png's, animationen, Text?
                                                                        # Wie können wir den Punkt Hass und Manipulation noch härter heimhämern?                                                               

        label Decision_stage_7:                     
            if Aggression >= 7:
                call screen Ending_1_Aggresive
            elif Aggression >=1 and Aggression <=6:
                call screen Ending_2_Fiesty
            elif Aggression >=-6 and Aggression <=0:
                call screen Ending_3_Diplomatic
            else:
                call screen Ending_4_Calming




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