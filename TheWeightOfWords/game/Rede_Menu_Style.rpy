screen Rede_Menu_Style:

    style_prefix "Decision_UI"

    frame:
        background None
        xalign 0.5
        yalign 0.5               
        add "UI/Speech_bg.png":
            xsize 2560
            ysize 1440

    frame:
        xpos 700
        ypos 10
        text "[which_decision]"
#
#    frame:
#        xpos 800
#        ypos 10 
#        vbox:
#            text"[Decisions]"
#
#    frame:
#        xpos 600
#        ypos 10
#        vbox:
#            text"[Aggression]"
#    
    frame:
        background None
        xpos 1730
        ypos 100
        vbox:
            xsize 700
            text"[Speech[0]]"
            text"[Speech[1]]"
            text"[Speech[2]]"
            text"[Speech[3]]"
            text"[Speech[4]]"
            text"[Speech[5]]"



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
    #    button:
    #        add Solid("#000")
    #        xsize 600
    #        ysize 100
    #        xpos 800
    #        ypos 1250
    #        xanchor .5
    #        hbox:
    #            text "Nachfolgen"
    #            xalign .5
    #            yalign .5
#
    #        action[
    #            Jump("Decision_stage_"+str(which_decision))
    #            ]




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
                    SetVariable("Which_decision", which_decision+1),
                    Jump("Decision_stage_"+str(which_decision))
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
                        text Rede1_Einstieg2
                    elif which_decision==2:
                        text Rede1_Reaktion2
                    elif which_decision==3:
                        text Rede1_Hinfuehrung2
                    elif which_decision==4:
                        text Rede1_Problem2
                    elif which_decision==5:
                        text Rede1_Erkenntnis2
                    else:
                        text Rede1_Aufruf2
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
                            text Rede1_Einstieg2:
                                color "#8b8a73"
                        elif which_decision==2:
                            text Rede1_Reaktion2:
                                color "#8b8a73"
                        elif which_decision==3:
                            text Rede1_Hinfuehrung2:
                                color "#8b8a73"
                        elif which_decision==4:
                            text Rede1_Problem2:
                                color "#8b8a73"
                        elif which_decision==5:
                            text Rede1_Erkenntnis2:
                                color "#8b8a73"
                        else:
                            text Rede1_Aufruf2:
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
                    SetVariable("Which_decision", which_decision+1),
                    Jump("Decision_stage_"+str(which_decision))
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
                        text Rede1_Einstieg1
                    elif which_decision==2:
                        text Rede1_Reaktion1
                    elif which_decision==3:
                        text Rede1_Hinfuehrung1
                    elif which_decision==4:
                        text Rede1_Problem1
                    elif which_decision==5:
                        text Rede1_Erkenntnis1
                    else:
                        text Rede1_Aufruf1

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
                            text Rede1_Einstieg1:
                                color "#8b8a73"
                        elif which_decision==2:
                            text Rede1_Reaktion1:
                                color "#8b8a73"
                        elif which_decision==3:
                            text Rede1_Hinfuehrung1:
                                color "#8b8a73"
                        elif which_decision==4:
                            text Rede1_Problem1:
                                color "#8b8a73"
                        elif which_decision==5:
                            text Rede1_Erkenntnis1:
                                color "#8b8a73"
                        else:
                            text Rede1_Aufruf1:
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
                    SetVariable("Which_decision", which_decision+1),
                    Jump("Decision_stage_"+str(which_decision))
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
                        text Rede1_Einstieg3
                    elif which_decision==2:
                        text Rede1_Reaktion3
                    elif which_decision==3:
                        text Rede1_Hinfuehrung3
                    elif which_decision==4:
                        text Rede1_Problem3
                    elif which_decision==5:
                        text Rede1_Erkenntnis3
                    else:
                        text Rede1_Aufruf3
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
                            text Rede1_Einstieg3:
                                color "#8b8a73"
                        elif which_decision==2:
                            text Rede1_Reaktion3:
                                color "#8b8a73"
                        elif which_decision==3:
                            text Rede1_Hinfuehrung3:
                                color "#8b8a73"
                        elif which_decision==4:
                            text Rede1_Problem3:
                                color "#8b8a73"
                        elif which_decision==5:
                            text Rede1_Erkenntnis3:
                                color "#8b8a73"
                        else:
                            text Rede1_Aufruf3:
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
                    SetVariable("Which_decision", which_decision+1),
                    Jump("Decision_stage_"+str(which_decision))
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
                        text Rede1_Einstieg4
                    elif which_decision==2:
                        text Rede1_Reaktion4
                    elif which_decision==3:
                        text Rede1_Hinfuehrung4
                    elif which_decision==4:
                        text Rede1_Problem4
                    elif which_decision==5:
                        text Rede1_Erkenntnis4
                    else:
                        text Rede1_Aufruf4
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
                            text Rede1_Einstieg4:
                                color "#8b8a73"
                        elif which_decision==2:
                            text Rede1_Reaktion4:
                                color "#8b8a73"
                        elif which_decision==3:
                            text Rede1_Hinfuehrung4:
                                color "#8b8a73"
                        elif which_decision==4:
                            text Rede1_Problem4:
                                color "#8b8a73"
                        elif which_decision==5:
                            text Rede1_Erkenntnis4:
                                color "#8b8a73"
                        else:
                            text Rede1_Aufruf4:
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
                text Rede1_Frage1:
                    color "#f1f0be"
            elif which_decision==2:
                text Rede1_Frage2:
                    color "#f1f0be"
            elif which_decision==3:
                text Rede1_Frage3:
                    color "#f1f0be"
            elif which_decision==4:
                text Rede1_Frage4:
                    color "#f1f0be"
            elif which_decision==5:
                text Rede1_Frage5:
                    color "#f1f0be"
            elif which_decision==6:
                text Rede1_Frage6:
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
                text "{size=*2}{color=#f1f0be}Nachfolgen"
                xalign .5
                yalign .5
            action[
                Jump("Decision_stage_"+str(which_decision))
                ]





style Decision_UI_text:
    size 20
    color"#524e44" 


########################################################################################################

label Audience_Reaction:
    call screen Publikum


screen Publikum:
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
            text"[Speech[0]]"
            text"[Speech[1]]"
            text"[Speech[2]]"
            text"[Speech[3]]"
            text"[Speech[4]]"
            text"[Speech[5]]"

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
            Jump ("Decision")
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
