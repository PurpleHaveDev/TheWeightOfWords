#Szenario 2 - Alles in einem 
label Szenario2:

    $Zeitungshöhe=0
    $which_decision=1
    if BriefingErfolgt == False:
        NA "Du bist Präsidentin eines Landes, das gar nicht so anders ist als unseres. Eine Krise erschüttert das Land, und du musst eine Rede halten, die zeigt, wohin es jetzt geht."
        NA "Bevor du auf die Bühne trittst, bekommst du noch ein paar Informationen: aus der Presse, aus den sozialen Medien und von den Geheimdiensten."
        NA "Lies sie dir in Ruhe durch, danach liegt es an dir, die richtigen Entscheidungen zu treffen."
        $BriefingErfolgt = True
    else:
        pass
    call screen Scenario2_Intro               
    
                                                                                                                 
label Sp2_Tutorial:
    NA "Jetzt kommt es auf dich an. Wähle die Bausteine für deine Rede aus, die du für richtig hältst."     
            
label Sp2_Decision:
    $Box_option_height = 600
    $Box_option_width = 600
    $Box_option_image_width = 900
    $Box_option_image_height = 500
    $Decision1 = True
    call screen Sp2_Rede_Menu_Style
    
label Sp2_Decision_stage_1:
    #$which_decision = which_decision+1
    while Decision1==True:
        if Decisions[0]==1:
            $Speech2[0] = Rede2_Einstieg1
            $Auswirkung[0] = Rede2_Lehre1_1
            $Publikum[0] = Rede2_Publikum1_1
            $Decision1 = False 
        elif Decisions[0]==2:
            $Speech2[0] = Rede2_Einstieg2
            $Auswirkung[0] = Rede2_Lehre1_2
            $Publikum[0] = Rede2_Publikum1_2
            $Decision1 = False                 
        elif Decisions[0]==3:
            $Speech2[0] = Rede2_Einstieg3
            $Auswirkung[0] = Rede2_Lehre1_3
            $Publikum[0] = Rede2_Publikum1_3
            $Decision1 = False 
        elif Decisions[0]==4:
            $Speech2[0] = Rede2_Einstieg4
            $Auswirkung[0] = Rede2_Lehre1_4
            $Publikum[0] = Rede2_Publikum1_4
            $Decision1 = False 
        else:
            pass
    $Decision2 = True
    jump Sp2_Audience_Reaction

label Sp2_Decision_stage_2:
    #$which_decision = which_decision+1        
    while Decision2==True:
        if Decisions[1]==1:
            $Speech2[1] = Rede2_Reaktion1
            $Auswirkung[1] = Rede2_Lehre2_1
            $Publikum[1] = Rede2_Publikum2_1
            $Decision2 = False
        elif Decisions[1]==2:
            $Speech2[1] = Rede2_Reaktion2
            $Auswirkung[1] = Rede2_Lehre2_2
            $Publikum[1] = Rede2_Publikum2_2
            $Decision2 = False
        elif Decisions[1]==3:
            $Speech2[1] = Rede2_Reaktion3
            $Auswirkung[1] = Rede2_Lehre2_3
            $Publikum[1] = Rede2_Publikum2_3
            $Decision2 = False
        elif Decisions[1]==4:
            $Speech2[1] = Rede2_Reaktion4
            $Auswirkung[1] = Rede2_Lehre2_4
            $Publikum[1] = Rede2_Publikum2_4
            $Decision2 = False
        else:
            pass
    $Decision3 = True
    jump Sp2_Audience_Reaction

label Sp2_Decision_stage_3:
    #$which_decision = which_decision+1
    while Decision3==True:
        if Decisions[2]==1:
            $Speech2[2] = Rede2_Hinfuehrung1
            $Auswirkung[2] = Rede2_Lehre3_1
            $Publikum[2] = Rede2_Publikum3_1
            $Decision3 = False 
        elif Decisions[2]==2:
            $Speech2[2] = Rede2_Hinfuehrung2
            $Auswirkung[2] = Rede2_Lehre3_2
            $Publikum[2] = Rede2_Publikum3_2
            $Decision3 = False 
        elif Decisions[2]==3:
            $Speech2[2] = Rede2_Hinfuehrung3
            $Auswirkung[2] = Rede2_Lehre3_3
            $Publikum[2] = Rede2_Publikum3_3
            $Decision3 = False 
        elif Decisions[2]==4:
            $Speech2[2] = Rede2_Hinfuehrung4
            $Auswirkung[2] = Rede2_Lehre3_4
            $Publikum[2] = Rede2_Publikum3_4
            $Decision3 = False 
        else:
            pass
    $Decision4 = True
    jump Sp2_Audience_Reaction

label Sp2_Decision_stage_4:
    #$which_decision = which_decision+1        
    while Decision4==True:
        if Decisions[3]==1:
            $Speech2[3] = Rede2_Problem1
            $Auswirkung[3] = Rede2_Lehre4_1
            $Publikum[3] = Rede2_Publikum4_1
            $Decision4 = False 
        elif Decisions[3]==2:
            $Speech2[3] = Rede2_Problem2
            $Auswirkung[3] = Rede2_Lehre4_2
            $Publikum[3] = Rede2_Publikum4_2
            $Decision4 = False 
        elif Decisions[3]==3:
            $Speech2[3] = Rede2_Problem3
            $Auswirkung[3] = Rede2_Lehre4_3
            $Publikum[3] = Rede2_Publikum4_3
            $Decision4 = False
        elif Decisions[3]==4:
            $Speech2[3] = Rede2_Problem4
            $Auswirkung[3] = Rede2_Lehre4_4
            $Publikum[3] = Rede2_Publikum4_4
            $Decision4 = False 
        else:
            pass
    $Decision5 = True
    jump Sp2_Audience_Reaction

label Sp2_Decision_stage_5:
    #$which_decision = which_decision+1
    while Decision5==True:
        if Decisions[4]==1:
            $Speech2[4] = Rede2_Erkenntnis1
            $Auswirkung[4] = Rede2_Lehre5_1
            $Publikum[4] = Rede2_Publikum5_1
            $Decision5 = False 
        elif Decisions[4]==2:
            $Speech2[4] = Rede2_Erkenntnis2
            $Auswirkung[4] = Rede2_Lehre5_2
            $Publikum[4] = Rede2_Publikum5_2
            $Decision5 = False 
        elif Decisions[4]==3:
            $Speech2[4] = Rede2_Erkenntnis3
            $Auswirkung[4] = Rede2_Lehre5_3
            $Publikum[4] = Rede2_Publikum5_3
            $Decision5 = False 
        elif Decisions[4]==4:
            $Speech2[4] = Rede2_Erkenntnis4
            $Auswirkung[4] = Rede2_Lehre5_4
            $Publikum[4] = Rede2_Publikum5_4
            $Decision5 = False 
        else:
            pass
    $Decision6 = True
    jump Sp2_Audience_Reaction

label Sp2_Decision_stage_6:
    #$which_decision = which_decision+1
    while Decision6==True:
        if Decisions[5]==1:
            $Speech2[5] = Rede2_Aufruf1
            $Auswirkung[5] = Rede2_Lehre6_1
            $Publikum[5] = Rede2_Publikum6_1
            $Decision6 = False
        elif Decisions[5]==2:
            $Speech2[5] = Rede2_Aufruf2
            $Auswirkung[5] = Rede2_Lehre6_2
            $Publikum[5] = Rede2_Publikum6_2
            $Decision6 = False
        elif Decisions[5]==3:
            $Speech2[5] = Rede2_Aufruf3
            $Auswirkung[5] = Rede2_Lehre6_3
            $Publikum[5] = Rede2_Publikum6_3
            $Decision6 = False
        elif Decisions[5]==4:
            $Speech2[5] = Rede2_Aufruf4
            $Auswirkung[5] = Rede2_Lehre6_4
            $Publikum[5] = Rede2_Publikum6_4
            $Decision6 = False
        else:
            pass
    jump Sp2_Audience_Reaction  

label Sp2_Decision_stage_7:                     
    if Aggression >= 7:
        call screen Ending_2o1_Aggresive
    elif Aggression >=1 and Aggression <=6:
        call screen Ending_2o2_Fiesty
    elif Aggression >=-6 and Aggression <=0:
        call screen Ending_2o3_Diplomatic
    else:
        call screen Ending_2o4_Calming






################################################################################################################################################

################################################################################################################################################

screen Scenario2_Intro:
    style_prefix "Sp2_Intro_UI"

    $Zeitungshöhe=0

    frame:
        background None
        xalign 0.5
        yalign 0.5               
        #add Solid ("#eb9e51")
        add "UI/Table_bg.png":
            xsize 2560
            ysize 1440
    frame:
        background None
        xalign 0.5
        yalign 0.5               
        add "UI/Pen&Coffee.png":
            xsize 2560
            ysize 1440
 
    imagebutton:
        xalign 0.7
        yalign 0.5  
        idle "UI/Zeitung_idle.png"
        hover "UI/Zeitung_hover.png"
        at Transform(zoom=1.32)
        focus_mask True
        action[
            Jump ("Sp2_Newspaper")
        ]

    imagebutton:
        xalign 0.5
        yalign 0.5  
        idle "UI/Geheimakte_idle.png"
        hover "UI/Geheimakte_hover.png"
        at Transform(zoom=1.32)
        focus_mask True
        action[
            Jump ("Sp2_Geheimakte")
        ]
 
    imagebutton:
        xalign 0.2
        yalign 0.5  
        idle "UI/Handy_idle.png"
        hover "UI/Handy_hover.png"
        at Transform(zoom=1.32)
        focus_mask True
        action[
            Jump ("Sp2_Smartphone")
        ]
 

 
 
    button:
        xpos 400
        ypos 1200
        frame:
            xalign 0.5
            yalign 0.5
            vbox:
                text "{color=#f1f0be}Auf zur Rede"
        action(
            SetVariable ("BriefingErfolgt", False),
            Jump ("Sp2_Tutorial")
        )

#77777777777777777777777777777777777777777777777777777777777777777777777777777777777
 
label Sp2_Geheimakte:
    call screen Sp2_Classified_Data

screen Sp2_Classified_Data:
    style_prefix "Geheimakte_öffnen"

    frame:
        background None
        xalign 0.5
        yalign 0.5               
        #add Solid ("#eb9e51")
        add "UI/Table_bg.png":
            xsize 2560
            ysize 1440

    frame:
        background None
        add "UI/Classified2.png"       

    button:
        xpos 100
        ypos 1200
        frame:
            xalign 0.5
            yalign 0.5
            vbox:
                text "<<< zurück"
        action Jump ("Szenario2")

#///////////////////////////////////////////////////////////////////////////////////////// 

label Sp2_Smartphone:
    call screen Sp2_Sc_Smartphone

screen Sp2_Sc_Smartphone:
    style_prefix "Social_Media_lesen"

    frame:
        background None
        xalign 0.5
        yalign 0.5               
        #add Solid ("#eb9e51")
        add "UI/Table_bg.png":
            xsize 2560
            ysize 1440

    frame:
        background None
        add "UI/Twitter2.png"       

    button:
        xpos 100
        ypos 1200
        frame:
            xalign 0.5
            yalign 0.5
            vbox:
                text "<<< zurück"
        action Jump ("Szenario2")

#///////////////////////////////////////////////////////////////////////////////

label Sp2_Newspaper:
    call screen Sp2_Sc_Newspaper

screen Sp2_Sc_Newspaper:
    style_prefix "Zeitung_lesen"

    frame:
        background None
        xalign 0.5
        yalign 0.5               
        #add Solid ("#eb9e51")
        add "UI/Table_bg.png":
            xsize 2560
            ysize 1440
    
    frame:
        background None
        add "UI/NWSPaper2.png":
            zoom 2
            xpos 540
            ypos Zeitungshöhe

    button:
        xpos 100
        ypos 1200
        frame:
            xalign 0.5
            yalign 0.5
            vbox:
                text "<<< zurück"
        action Jump ("Szenario2")

    button:
        add Solid ("#2c2412")
        xsize 300
        ysize 100
        xanchor .5
        yanchor .5
        xpos 1300
        ypos 100
        vbox:
            yalign .5
            xalign .5
            text "^"
        action[
            SetVariable ("Zeitungshöhe",Zeitungshöhe+100),
            Jump("Sp2_Newspaper")
        ] 

    button:
        add Solid ("#2c2412")
        xsize 300
        ysize 100
        xanchor .5
        yanchor .5
        xpos 1300
        ypos 1300
        vbox:
            yalign .5
            xalign .5
            text "v"
        action[
            SetVariable ("Zeitungshöhe",Zeitungshöhe-100),
            Jump("Sp2_Newspaper")
        ] 



####################################################################################################

####################################################################################################


label Sp2_Audience_Reaction:
    call screen Sp2_Publikum


screen Sp2_Publikum:
    style_prefix "Audience"


    frame:
        background None
        xalign 0.5
        yalign 0.5               
        add "UI/Speech_bg.png":
            xsize 2560
            ysize 1440

    frame:
        background None
        xpos 1730
        ypos 100
        vbox:
            xsize 700
            text"[Speech2[0]]"
            text"[Speech2[1]]"
            text"[Speech2[2]]"
            text"[Speech2[3]]"
            text"[Speech2[4]]"
            text"[Speech2[5]]"

    frame:
        background None
        xalign 0.5
        yalign 0.5               
        add "UI/Audience_Back.png":
            xsize 2560
            ysize 1440
            xanchor 1
            xzoom -1

    frame:
        background None
        xalign 0.5
        yalign 0.5               
        add "UI/Audience_Front.png":
            xsize 2560
            ysize 1440

    button:
        xpos 500
        ypos 1300
        frame:
            xalign 0.5
            yalign 0.5
            vbox:
                text "{color=#f1f0be}Weiter >>>"
        action(
            SetVariable ("Page",1),
            Jump ("Sp2_Decision")
        )
        
    if which_decision==2:
        frame:
            xpos 50
            ypos 1100
            vbox:
                xalign .5
                yalign .5
                xsize 1500
                text Publikum[0]

    elif which_decision==3:
        frame:
            xpos 50
            ypos 1100
            vbox:
                xalign .5
                yalign .5
                xsize 1500
                text Publikum[1]

    elif which_decision==4:
        frame:
            xpos 50
            ypos 1100
            vbox:
                xalign .5
                yalign .5
                xsize 1500
                text Publikum[2]

    elif which_decision==5:
        frame:
            xpos 50
            ypos 1100
            vbox:
                xalign .5
                yalign .5
                xsize 1500
                text Publikum[3]

    elif which_decision==6:
        frame:
            xpos 50
            ypos 1100
            vbox:
                xalign .5
                yalign .5
                xsize 1500
                text Publikum[4]

    else:
        frame:
            xpos 50
            ypos 1100
            vbox:
                xalign .5
                yalign .5
                xsize 1500
                text Publikum[5]


##########################################################################################################

###########################################################################################################

screen Sp2_Rede_Menu_Style:

    style_prefix "Decision_UI2"

    frame:
        background None
        xalign 0.5
        yalign 0.5               
        add "UI/Speech_bg.png":
            xsize 2560
            ysize 1440

    frame:
        background None
        xpos 1730
        ypos 100
        vbox:
            xsize 700
            text"[Speech2[0]]"
            text"[Speech2[1]]"
            text"[Speech2[2]]"
            text"[Speech2[3]]"
            text"[Speech2[4]]"
            text"[Speech2[5]]"



    frame:
        background None
        xalign 0.5
        yalign 0.5               
        add "UI/Audience_Back.png":
            xsize 2560
            ysize 1440
            xanchor 1
            xzoom -1


    if which_decision>=7:
        pass

###########################################################################################

    else:     

        if which_decision<=2 or Aggression>-4:
     
            imagebutton:
                idle "UI/Choice2_idle.png"
                hover "UI/Choice2_hover.png"
                focus_mask True                                      

                action[
                    Function(Decisions.__setitem__,which_decision - 1, 2),
                    SetVariable("Aggression", Aggression+2),
                    SetVariable("which_decision", which_decision+1),
                    Jump("Sp2_Decision_stage_"+str(which_decision))
                ]
            

            frame:
                background None
                xpos 930
                ypos 270
                vbox:                                                                                  
                    xalign 0.5                                   
                    yalign 0.5
                    xsize 500
                    if which_decision==1:
                        text Rede2_Einstieg2
                    elif which_decision==2:
                        text Rede2_Reaktion2
                    elif which_decision==3:
                        text Rede2_Hinfuehrung2
                    elif which_decision==4:
                        text Rede2_Problem2
                    elif which_decision==5:
                        text Rede2_Erkenntnis2
                    else:
                        text Rede2_Aufruf2
        else:
            frame:
                background None
                add "UI/Choice2_idle.png":
                    alpha 0.5    
                    xalign 0.5
                    yalign 0.5
                frame:
                    background None
                    xpos 930
                    ypos 270
                    vbox:                                                                                  
                        xalign 0.5                                   
                        yalign 0.5
                        xsize 500
                        if which_decision==1:
                            text Rede2_Einstieg2:
                                color "#8b8a73"
                        elif which_decision==2:
                            text Rede2_Reaktion2:
                                color "#8b8a73"
                        elif which_decision==3:
                            text Rede2_Hinfuehrung2:
                                color "#8b8a73"
                        elif which_decision==4:
                            text Rede2_Problem2:
                                color "#8b8a73"
                        elif which_decision==5:
                            text Rede2_Erkenntnis2:
                                color "#8b8a73"
                        else:
                            text Rede2_Aufruf2:
                                color "#8b8a73"

################################################################################################


        if which_decision<=2 or Aggression>-6 and Aggression<8:
            imagebutton:
                idle "UI/Choice1_idle.png"
                hover "UI/Choice1_hover.png"
                focus_mask True  
                action[
                    Function(Decisions.__setitem__,which_decision - 1, 1),
                    SetVariable("Aggression", Aggression+1),
                    SetVariable("which_decision", which_decision+1),
                    Jump("Sp2_Decision_stage_"+str(which_decision))
                ]
            frame:
                background None
                xpos 200
                ypos 270
                vbox:                                                                                  
                    xalign 0.5                                   
                    yalign 0.5
                    xsize 500
                    if which_decision==1:
                        text Rede2_Einstieg1
                    elif which_decision==2:
                        text Rede2_Reaktion1
                    elif which_decision==3:
                        text Rede2_Hinfuehrung1
                    elif which_decision==4:
                        text Rede2_Problem1
                    elif which_decision==5:
                        text Rede2_Erkenntnis1
                    else:
                        text Rede2_Aufruf1

        else:
            frame:
                background None
                add "UI/Choice1_idle.png":
                    alpha 0.5    
                    xalign 0.5
                    yalign 0.5
                frame:
                    background None
                    xpos 200
                    ypos 270
                    vbox:                                                                                  
                        xalign 0.5                                   
                        yalign 0.5
                        xsize 500
                        if which_decision==1:
                            text Rede2_Einstieg1:
                                color "#8b8a73"
                        elif which_decision==2:
                            text Rede2_Reaktion1:
                                color "#8b8a73"
                        elif which_decision==3:
                            text Rede2_Hinfuehrung1:
                                color "#8b8a73"
                        elif which_decision==4:
                            text Rede2_Problem1:
                                color "#8b8a73"
                        elif which_decision==5:
                            text Rede2_Erkenntnis1:
                                color "#8b8a73"
                        else:
                            text Rede2_Aufruf1:
                                color "#8b8a73"
        
###########################################################################################################        
        
        if which_decision<=2 or Aggression>-8 and Aggression<6:
            imagebutton:
                idle "UI/Choice3_idle.png"
                hover "UI/Choice3_hover.png"
                focus_mask True 

                action[
                    Function(Decisions.__setitem__,which_decision - 1, 3),
                    SetVariable("Aggression", Aggression-1),
                    SetVariable("which_decision", which_decision+1),
                    Jump("Sp2_Decision_stage_"+str(which_decision))
                ]
            frame:
                background None
                xpos 200
                ypos 850
                vbox:                                                                                  
                    xalign 0.5                                   
                    yalign 0.5
                    xsize 500
                    if which_decision==1:
                        text Rede2_Einstieg3
                    elif which_decision==2:
                        text Rede2_Reaktion3
                    elif which_decision==3:
                        text Rede2_Hinfuehrung3
                    elif which_decision==4:
                        text Rede2_Problem3
                    elif which_decision==5:
                        text Rede2_Erkenntnis3
                    else:
                        text Rede2_Aufruf3
        else:
            frame:
                background None
                add "UI/Choice3_idle.png":
                    alpha 0.5    
                    xalign 0.5
                    yalign 0.5
                frame:
                    background None
                    xpos 200
                    ypos 850
                    vbox:                                                                                  
                        xalign 0.5                                   
                        yalign 0.5
                        xsize 500
                        if which_decision==1:
                            text Rede2_Einstieg3:
                                color "#8b8a73"
                        elif which_decision==2:
                            text Rede2_Reaktion3:
                                color "#8b8a73"
                        elif which_decision==3:
                            text Rede2_Hinfuehrung3:
                                color "#8b8a73"
                        elif which_decision==4:
                            text Rede2_Problem3:
                                color "#8b8a73"
                        elif which_decision==5:
                            text Rede2_Erkenntnis3:
                                color "#8b8a73"
                        else:
                            text Rede2_Aufruf3:
                                color "#8b8a73"
            
#########################################################################################################

        if which_decision<=2 or Aggression<4:
            imagebutton:
                idle "UI/Choice4_idle.png"
                hover "UI/Choice4_hover.png"
                focus_mask True 
                action[
                    Function(Decisions.__setitem__,which_decision - 1, 4),
                    SetVariable("Aggression", Aggression-2),
                    SetVariable("which_decision", which_decision+1),
                    Jump("Sp2_Decision_stage_"+str(which_decision))
                ]
            frame:
                background None
                xpos 930
                ypos 850
                vbox:                                                                                  
                    xalign 0.5                                   
                    yalign 0.5
                    xsize 500
                    if which_decision==1:
                        text Rede2_Einstieg4
                    elif which_decision==2:
                        text Rede2_Reaktion4
                    elif which_decision==3:
                        text Rede2_Hinfuehrung4
                    elif which_decision==4:
                        text Rede2_Problem4
                    elif which_decision==5:
                        text Rede2_Erkenntnis4
                    else:
                        text Rede2_Aufruf4
        else:
            frame:
                background None
                add "UI/Choice4_idle.png":
                    alpha 0.5    
                    xalign 0.5
                    yalign 0.5
                frame:
                    background None
                    xpos 930
                    ypos 850
                    vbox:                                                                                  
                        xalign 0.5                                   
                        yalign 0.5
                        xsize 500
                        if which_decision==1:
                            text Rede2_Einstieg4:
                                color "#8b8a73"
                        elif which_decision==2:
                            text Rede2_Reaktion4:
                                color "#8b8a73"
                        elif which_decision==3:
                            text Rede2_Hinfuehrung4:
                                color "#8b8a73"
                        elif which_decision==4:
                            text Rede2_Problem4:
                                color "#8b8a73"
                        elif which_decision==5:
                            text Rede2_Erkenntnis4:
                                color "#8b8a73"
                        else:
                            text Rede2_Aufruf4:
                                color "#8b8a73"


    frame:
        background None
        xalign 0.5
        yalign 0.5               
        add "UI/Audience_Front.png":
            xsize 2560
            ysize 1440
    
    frame:
        add Solid("#000")
        xsize 1100
        ysize 100
        xpos 800
        ypos 1250
        xanchor .5
        hbox:
            xalign .5
            yalign .5
            if which_decision==1:
                text Rede2_Frage1:
                    color "#f1f0be"
            elif which_decision==2:
                text Rede2_Frage2:
                    color "#f1f0be"
            elif which_decision==3:
                text Rede2_Frage3:
                    color "#f1f0be"
            elif which_decision==4:
                text Rede2_Frage4:
                    color "#f1f0be"
            elif which_decision==5:
                text Rede2_Frage5:
                    color "#f1f0be"
            elif which_decision==6:
                text Rede2_Frage6:
                    color "#f1f0be"
            else:
                pass


    if which_decision == 7:
        button:
            add Solid("#000")
            xsize 1100
            ysize 100
            xpos 800
            ypos 1250
            xanchor .5
            hbox:
                text "{size=*2}{color=#f1f0be}Viele Jahre später ..."
                xalign .5
                yalign .5
            action[
                Jump("Sp2_Decision_stage_"+str(which_decision))
                ]

#####################################################################################################################

#####################################################################################################################

screen Ending_2o1_Aggresive:
    style_prefix "end1"

    frame:
        background None
        xalign 0.5
        yalign 0.5
        add "UI/End_Aggressiv.png":
            xsize 2560
            ysize 1440
        vbox:
            xpos 1550
            ypos 180
            xsize 800
            text "{size=*.8}{color=#000}Das Kabinett verhängte wenige Tage nach der Rede erste Zölle und Kapitalsperren gegen die Nachbarstaaten. Was die heimische Wirtschaft eigentlich unterstützen sollte, würde zu einer Katastrophe für Unternehmen und die Menschen im Land."
            text "{size=*.8}{color=#000}Lieferketten brachen zusammen, ganze Branchen verschwanden. Misstrauen gegen alles Ausländische fraß sich durch die Gesellschaft. In der Forschung gilt die Rede zur Nordbank-Krise als der Wendepunkt,"
            text "{size=*.8}{color=#000}an dem der Weg in diese wirtschaftliche Isolation eingeschlagen wurde. Noch heute, Jahrzehnte später, ist das Land wirtschaftlich abgeschottet."
            text "{size=*.8}{color=#000}Immer wiederkehrende Handelskonflikte und Versorgungskrisen definieren Politik und Alltag."

    frame:
        xanchor .5
        yanchor .5
        xsize 600
        ysize 120
        xpos 650
        ypos 150
        hbox:
            xalign .5
            yalign .5
            text "{size=*1.8}{color=#f1f0be}Aggressiv"            

    button:
        xpos 500
        ypos 1300
        frame:
            xalign 0.5
            yalign 0.5
            vbox:
                text "{color=#f1f0be}Weiter >>>"
        action[
            SetVariable ("Page",1),
            Jump ("Sp2_Erklärung")
        ]



screen Ending_2o2_Fiesty:
    style_prefix "end2"

    frame:
        background None
        xalign 0.5
        yalign 0.5
        add "UI/End_Kaempferisch.png":
            xsize 2560
            ysize 1440
        vbox:
            xpos 1550
            ypos 180
            xsize 800
            text "{size=*0.87}{color=#000}Die Ermittlungen nach dem Zusammenbruch der Nordbank führten zu Anklagen. Die Netzwerke aus Missmanagement und Bilanzbetrug wurden aufgedeckt und zerschlagen."
            text "{size=*0.87}{color=#000}Das Vertrauen in den Staat stieg in großen Teilen der Bevölkerung. Doch obwohl die Schuldigen ermittelt wurden und einige neue Regeln aufgestellt wurden, hielten sich nicht alle Unternehmen daran."
            text "{size=*0.87}{color=#000}Außerdem hatte die Krise viele Bürgerinnen und Bürger stark gebeutelt und einfachere Arbeiterinnen und Arbeiter hatten am Ende des Monats Kaum noch Geld zur Verfügung."
            text "{size=*0.87}{color=#000}Die Schuld dafür suchten Opposition und Unzufriedene wahlweise in Ausländern, Minderheiten oder dem System an sich."
            text "{size=*0.87}{color=#000}Trotzdem erholte sich das Land nach einigen Jahren von der Nordbank-Krise, die Rede der Präsidentin hatte den Grundstein gelegt."

    frame:
        xanchor .5
        yanchor .5
        xsize 600
        ysize 120
        xpos 650
        ypos 150
        hbox:
            xalign .5
            yalign .5
            text "{size=*1.8}{color=#f1f0be}Kämpferisch"

    button:
        xpos 500
        ypos 1300
        frame:
            xalign 0.5
            yalign 0.5
            vbox:
                text "{color=#f1f0be}Weiter >>>"
        action[
            SetVariable ("Page",1),
            Jump ("Sp2_Erklärung")
        ]


screen Ending_2o3_Diplomatic:
    style_prefix "end3"

    frame:
        background None
        xalign 0.5
        yalign 0.5
        add "UI/End_Versoehnend.png":
            xsize 2560
            ysize 1440
        vbox:
            xpos 1550
            ypos 180
            xsize 800
            text "{size=*0.9}{color=#000}Die gesellschaftliche Spaltung entlang von Arm und Reich, die viele nach dem Bankencrash befürchtet hatten, blieb aus. In öffentlichen Debatten rang das Land um das Ausmaß der Hilfe für sozial Benachteiligte in der Krise. "
            text "{size=*0.9}{color=#000}Es wurde über neue Regeln debattiert und schließlich wurden Markt und Wirtschaft mit rigorosen Auflagen belegt. Das führte zu weniger Wachstum, aber auch zu weniger Missbrauch."
            text "{size=*0.9}{color=#000}Nach der Krise fühlten sich viele Menschen in diesem harten Kurs bestätigt. Doch der Weg blieb aufgrund der Einschränkungen wirtschaftlich steinig und es kam immer wieder zu Verteilungsproblemen."
            text "{size=*0.9}{color=#000}Dennoch erholte sich das Land von der Krise und die Rede der Präsidentin wurde als Grundstein für diesen Weg angesehen."

    frame:
        xanchor .5
        yanchor .5
        xsize 600
        ysize 120
        xpos 650
        ypos 150
        hbox:
            xalign .5
            yalign .5
            text "{size=*1.8}{color=#f1f0be}Versöhnend"

    button:
        xpos 500
        ypos 1300
        frame:
            xalign 0.5
            yalign 0.5
            vbox:
                text "{color=#f1f0be}Weiter >>>"
        action[
            SetVariable ("Page",1),
            Jump ("Sp2_Erklärung")
        ]



screen Ending_2o4_Calming:
    style_prefix "end4"

    frame:
        background None
        xalign 0.5
        yalign 0.5
        add "UI/End_Beschwichtigend.png":
            xsize 2560
            ysize 1440
        vbox:
            xpos 1550
            ypos 180
            xsize 800
            text "{size=*0.8}{color=#000}In den Monaten nach dem Zusammenbruch der Nordbank schoben sich die politischen Lager gegenseitig die Verantwortung zu. Eine klare Linie blieb aus."
            text "{size=*0.8}{color=#000}Das Vertrauen in Banken und Institutionen sank. Die Menschen holten ihr Kapital aus den Banken ab und hoben massenweise Geld ab. Der Kurs von Gold und anderen krisenfesten Anlagen schoss in die Höhe."
            text "{size=*0.8}{color=#000}Durch den Kapitalabfluss setzte ein Dominoeffekt ein und etliche Banken stürzten nach der Nordbank in die Krise. Die Krise wuchs sich zu einer Weltwirtschaftskrise aus,"
            text "{size=*0.8}{color=#000}von der sich das Land bis heute nicht erholt hat. Immer wieder kommt es zu Umstürzen im politischen System,"
            text "{size=*0.8}{color=#000}und die extrempolitischen Ränder sind gerade bei den jungen Menschen, die von der Krise gebeutelt wurden, sehr beliebt."
            text "{size=*0.8}{color=#000}Die Rede der Präsidentin gilt als Ausgangspunkt für dieses Versagen."

    frame:
        xanchor .5
        yanchor .5
        xsize 700
        ysize 120
        xpos 650
        ypos 150
        hbox:
            xalign .5
            yalign .5
            text "{size=*1.8}{color=#f1f0be}Beschwichtigend"

    button:
        xpos 500
        ypos 1300
        frame:
            xalign 0.5
            yalign 0.5
            vbox:
                text "{color=#f1f0be}Weiter >>>"
        action(
            SetVariable ("Page",1),
            Jump ("Sp2_Erklärung")
        )


##########################################################################################################################

##########################################################################################################################


label Sp2_Erklärung:
    call screen Sp2_ErklärungScreen

screen Sp2_ErklärungScreen: 
    style_prefix "Sp2_Diagramm"

    frame:
        background None
        xalign 0.5
        yalign 0.5               
        add "UI/Screen_Erklärung.png":
            xsize 2560
            ysize 1440  

    if Page==1:

        imagebutton:
            xalign 0.5
            yalign 0.5  
            idle "UI/Next_Arw.png"
            hover "UI/Next_Arw.png"
            focus_mask True
            action[
                SetVariable ("Page",2),
                Jump ("Sp2_Erklärung")
            ]
        
        button:
            xpos 1200
            ypos 1325
            frame:
                xalign 0.5
                yalign 0.5
                vbox:
                    text "{color=#f1f0be}Home"
            action(
                SetVariable("Speech2", ["","","","","",""]),
                SetVariable("Auswirkung", ["","","","","",""]),
                Jump ("start")
            )



        vbox:
            xpos 300
            ypos 200
            xsize 500
            text Speech2[0]:
                #size 30
                color "#000"             
        vbox:
            xpos 1050
            ypos 200
            xsize 500
            text Speech2[1]:
                #size 30
                color "#000"
        vbox:
            xpos 1790
            ypos 200
            xsize 500
            text Speech2[2]:
                #size 30
                color "#000"



        vbox:
            xpos 300
            ypos 975
            xsize 500
            text "[Auswirkung[0]]":
                size 30
                color "#000"         
        vbox:
            xpos 1050
            ypos 1000
            xsize 500
            text "[Auswirkung[1]]":
                size 30
                color "#000"
        vbox:
            xpos 1790
            ypos 1000
            xsize 500
            text "[Auswirkung[2]]":
                size 30
                color "#000"

        
    else:

        imagebutton:
            xalign 0.5
            yalign 0.5  
            idle "UI/Previous_Arw.png"
            hover "UI/Previous_Arw.png"
            focus_mask True
            action[
                SetVariable ("Page",1)
            ]

        vbox:
            xpos 300
            ypos 200
            xsize 500
            text Speech2[3]:
                #size 30
                color "#000"             
        vbox:
            xpos 1050
            ypos 200
            xsize 500
            text Speech2[4]:
                #size 30
                color "#000"
        vbox:
            xpos 1790
            ypos 200
            xsize 500
            text Speech2[5]:
                #size 30
                color "#000"



        vbox:
            xpos 300
            ypos 1000
            xsize 500
            text "[Auswirkung[3]]":
                size 30
                color "#000"         
        vbox:
            xpos 1050
            ypos 1000
            xsize 500
            text "[Auswirkung[4]]":
                size 30
                color "#000"
        vbox:
            xpos 1790
            ypos 1000
            xsize 500
            text "[Auswirkung[5]]":
                size 30
                color "#000"
        button:
            xpos 1200
            ypos 1325
            frame:
                xalign 0.5
                yalign 0.5
                vbox:
                    text "{color=#f1f0be}Home"
            action(
                SetVariable("Speech2", ["","","","","",""]),
                SetVariable("Auswirkung", ["","","","","",""]),
                Jump ("start")
            )