
label Szenario1:
    if English==False:  
        $Zeitungshöhe=0
        $Handyhöhe=0
        $Aktenhöhe=0
        $which_decision=1


        if BriefingErfolgt == False:
            NA "Du bist Präsidentin eines Landes, das gar nicht so anders ist als unseres. Eine Krise erschüttert das Land, und du musst eine Rede halten, die zeigt, wohin es jetzt geht."
            NA "Bevor du auf die Bühne trittst, bekommst du noch ein paar Informationen: aus der Presse, aus den sozialen Medien und von den Geheimdiensten."
            NA "Lies sie dir in Ruhe durch, danach liegt es an dir, die richtigen Entscheidungen zu treffen."
            $BriefingErfolgt = True
        else:
            pass
        call screen Scenario1_Intro                                                                        #Hier ist das setup des szenarios in Form eines Zeitzungsartikels

        label Tutorial:
            NA "Jetzt kommt es auf dich an. Wähle die Bausteine für deine Rede aus, die du für richtig hältst."                                                                   #Anleitung zum kommenden Gameplay

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
                    $Auswirkung[0] = Rede1_Lehre1_1
                    $Publikum[0] = Rede1_Publikum1_1
                    $Decision1 = False 
                elif Decisions[0]==2:
                    $Speech[0] = Rede1_Einstieg2
                    $Auswirkung[0] = Rede1_Lehre1_2
                    $Publikum[0] = Rede1_Publikum1_2
                    $Decision1 = False                 
                elif Decisions[0]==3:
                    $Speech[0] = Rede1_Einstieg3
                    $Auswirkung[0] = Rede1_Lehre1_3
                    $Publikum[0] = Rede1_Publikum1_3
                    $Decision1 = False 
                elif Decisions[0]==4:
                    $Speech[0] = Rede1_Einstieg4
                    $Auswirkung[0] = Rede1_Lehre1_4
                    $Publikum[0] = Rede1_Publikum1_4
                    $Decision1 = False 
                else:
                    pass
            $Decision2 = True
            jump Audience_Reaction

        label Decision_stage_2:
            $which_decision = which_decision+1        
            $Function(renpy.notify, "Das klappt2")
            while Decision2==True:
                if Decisions[1]==1:
                    $Speech[1] = Rede1_Reaktion1
                    $Auswirkung[1] = Rede1_Lehre2_1
                    $Publikum[1] = Rede1_Publikum2_1
                    $Decision2 = False
                elif Decisions[1]==2:
                    $Speech[1] = Rede1_Reaktion2
                    $Auswirkung[1] = Rede1_Lehre2_2
                    $Publikum[1] = Rede1_Publikum2_2
                    $Decision2 = False
                elif Decisions[1]==3:
                    $Speech[1] = Rede1_Reaktion3
                    $Auswirkung[1] = Rede1_Lehre2_3
                    $Publikum[1] = Rede1_Publikum2_3
                    $Decision2 = False
                elif Decisions[1]==4:
                    $Speech[1] = Rede1_Reaktion4
                    $Auswirkung[1] = Rede1_Lehre2_4
                    $Publikum[1] = Rede1_Publikum2_4
                    $Decision2 = False
                else:
                    pass
            $Decision3 = True
            jump Audience_Reaction

        label Decision_stage_3:
            $which_decision = which_decision+1
            $Function(renpy.notify, "Das klappt3")
            while Decision3==True:
                if Decisions[2]==1:
                    $Speech[2] = Rede1_Hinfuehrung1
                    $Auswirkung[2] = Rede1_Lehre3_1
                    $Publikum[2] = Rede1_Publikum3_1
                    $Decision3 = False 
                elif Decisions[2]==2:
                    $Speech[2] = Rede1_Hinfuehrung2
                    $Auswirkung[2] = Rede1_Lehre3_2
                    $Publikum[2] = Rede1_Publikum3_2
                    $Decision3 = False 
                elif Decisions[2]==3:
                    $Speech[2] = Rede1_Hinfuehrung3
                    $Auswirkung[2] = Rede1_Lehre3_3
                    $Publikum[2] = Rede1_Publikum3_3
                    $Decision3 = False 
                elif Decisions[2]==4:
                    $Speech[2] = Rede1_Hinfuehrung4
                    $Auswirkung[2] = Rede1_Lehre3_4
                    $Publikum[2] = Rede1_Publikum3_4
                    $Decision3 = False 
                else:
                    pass
            $Decision4 = True
            jump Audience_Reaction

        label Decision_stage_4:
            $which_decision = which_decision+1        
            $Function(renpy.notify, "Das klappt4")
            while Decision4==True:
                if Decisions[3]==1:
                    $Speech[3] = Rede1_Problem1
                    $Auswirkung[3] = Rede1_Lehre4_1
                    $Publikum[3] = Rede1_Publikum4_1
                    $Decision4 = False 
                elif Decisions[3]==2:
                    $Speech[3] = Rede1_Problem2
                    $Auswirkung[3] = Rede1_Lehre4_2
                    $Publikum[3] = Rede1_Publikum4_2
                    $Decision4 = False 
                elif Decisions[3]==3:
                    $Speech[3] = Rede1_Problem3
                    $Auswirkung[3] = Rede1_Lehre4_3
                    $Publikum[3] = Rede1_Publikum4_3
                    $Decision4 = False
                elif Decisions[3]==4:
                    $Speech[3] = Rede1_Problem4
                    $Auswirkung[3] = Rede1_Lehre4_4
                    $Publikum[3] = Rede1_Publikum4_4
                    $Decision4 = False 
                else:
                    pass
            $Decision5 = True
            jump Audience_Reaction

        label Decision_stage_5:
            $which_decision = which_decision+1
            $Function(renpy.notify, "Das klappt5")
            while Decision5==True:
                if Decisions[4]==1:
                    $Speech[4] = Rede1_Erkenntnis1
                    $Auswirkung[4] = Rede1_Lehre5_1
                    $Publikum[4] = Rede1_Publikum5_1
                    $Decision5 = False 
                elif Decisions[4]==2:
                    $Speech[4] = Rede1_Erkenntnis2
                    $Auswirkung[4] = Rede1_Lehre5_2
                    $Publikum[4] = Rede1_Publikum5_2
                    $Decision5 = False 
                elif Decisions[4]==3:
                    $Speech[4] = Rede1_Erkenntnis3
                    $Auswirkung[4] = Rede1_Lehre5_3
                    $Publikum[4] = Rede1_Publikum5_3
                    $Decision5 = False 
                elif Decisions[4]==4:
                    $Speech[4] = Rede1_Erkenntnis4
                    $Auswirkung[4] = Rede1_Lehre5_4
                    $Publikum[4] = Rede1_Publikum5_4
                    $Decision5 = False 
                else:
                    pass
            $Decision6 = True
            jump Audience_Reaction

        label Decision_stage_6:
            $which_decision = which_decision+1
            $Function(renpy.notify, "Das klappt6")
            while Decision6==True:
                if Decisions[5]==1:
                    $Speech[5] = Rede1_Aufruf1
                    $Auswirkung[5] = Rede1_Lehre6_1
                    $Publikum[5] = Rede1_Publikum6_1
                    $Decision6 = False
                elif Decisions[5]==2:
                    $Speech[5] = Rede1_Aufruf2
                    $Auswirkung[5] = Rede1_Lehre6_2
                    $Publikum[5] = Rede1_Publikum6_2
                    $Decision6 = False
                elif Decisions[5]==3:
                    $Speech[5] = Rede1_Aufruf3
                    $Auswirkung[5] = Rede1_Lehre6_3
                    $Publikum[5] = Rede1_Publikum6_3
                    $Decision6 = False
                elif Decisions[5]==4:
                    $Speech[5] = Rede1_Aufruf4
                    $Auswirkung[5] = Rede1_Lehre6_4
                    $Publikum[5] = Rede1_Publikum6_4
                    $Decision6 = False

                else:
                    pass
            jump Audience_Reaction                                                        

        label Decision_stage_7:                     
            if Aggression >= 7:
                call screen Ending_1o1_Aggresive
            elif Aggression >=1 and Aggression <=6:
                call screen Ending_1o2_Fiesty
            elif Aggression >=-6 and Aggression <=0:
                call screen Ending_1o3_Diplomatic
            else:
                call screen Ending_1o4_Calming




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