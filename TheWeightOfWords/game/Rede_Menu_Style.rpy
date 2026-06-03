screen Rede_Menu_Style:

    style_prefix "Decision_UI"

    frame:
        xpos 700
        ypos 10
        text "[which_decision]"

    frame:
        xpos 800
        ypos 10
        vbox:
            text"[Decisions]"

    frame:
        xpos 600
        ypos 10
        vbox:
            text"[Aggression]"
    
    frame:
        xpos 2000
        ypos 10
        vbox:
            text"[Speech[0]]"
            text"[Speech[1]]"
            text"[Speech[2]]"
            text"[Speech[3]]"
            text"[Speech[4]]"
            text"[Speech[5]]"


    button:
        xpos 200
        ypos 100
        frame:
            xpadding 15                                                                               #fügt nen coushion rahmen um den text
            ypadding 15                                                                               #ACHTUNG: Das affected nur den Text, nicht den rahmen selbst. Anstatt den rahmen größer zu machen, skaliert es den Text nach innen
            #add Solid ("#b1a688")
            add "UI/paper.png":
                xsize Box_option_image_width
                ysize Box_option_image_height
                xalign 0.5
                yalign 0.5
            xsize Box_option_width
            ysize Box_option_height                                                  
            vbox:                                                                                    # vbox and hbox for vertical and horizontally aligned text respectively                                                
                xalign 0.5                                                                              # use (grid "width" "height":) for combined hbox and vbox aka. a Grid
                yalign 0.5
                if which_decision==1:
                    text "[Rede1_Einstieg1]"
                elif which_decision==2:
                    text "[Rede1_Reaktion1]"
                elif which_decision==3:
                    text "[Rede1_Hinführung1]"
                elif which_decision==4:
                    text "[Rede1_Problem1]"
                elif which_decision==5:
                    text "[Rede1_Erkenntnis1]"
                else:
                    text "[Rede1_Aufruf1]"
        action[
            Function(Decisions.__setitem__,which_decision - 1, 1),
            SetVariable("Aggression", Aggression+1),
            SetVariable("Which_decision", which_decision+1),
            #Jump(expression="Decision_stage_"+str(which_decision))
            Jump("Decision_stage_1")
        ]
        

    button:
        xpos 800
        ypos 100
        frame:
            xpadding 15               
            ypadding 15               
            #add Solid ("#b1a688")
            add "UI/paper.png":
                xsize Box_option_image_width
                ysize Box_option_image_height
                xalign 0.5
                yalign 0.5
            xsize Box_option_width
            ysize Box_option_height                                                  
            vbox:                                                                                  
                xalign 0.5                                   
                yalign 0.5
                if which_decision==1:
                    text "[Rede1_Einstieg2]"
                elif which_decision==2:
                    text "[Rede1_Reaktion2]"
                elif which_decision==3:
                    text "[Rede1_Hinführung2]"
                elif which_decision==4:
                    text "[Rede1_Problem2]"
                elif which_decision==5:
                    text "[Rede1_Erkenntnis2]"
                else:
                    text "[Rede1_Aufruf2]"
        action[
            Function(Decisions.__setitem__,which_decision - 1, 2),
            SetVariable("Aggression", Aggression+2),
            SetVariable("Which_decision", which_decision+1),
            #Jump(expression="Decision_stage_"+str(which_decision))
        ]

    button:
        xpos 200
        ypos 700
        frame:
            xpadding 15               
            ypadding 15               
            #add Solid ("#b1a688")
            add "UI/paper.png":
                xsize Box_option_image_width
                ysize Box_option_image_height
                xalign 0.5
                yalign 0.5
            xsize Box_option_width
            ysize Box_option_height                                                  
            vbox:                                           
                xalign 0.5                                   
                yalign 0.5
                if which_decision==1:
                    text "[Rede1_Einstieg3]"
                elif which_decision==2:
                    text "[Rede1_Reaktion3]"
                elif which_decision==3:
                    text "[Rede1_Hinführung3]"
                elif which_decision==4:
                    text "[Rede1_Problem3]"
                elif which_decision==5:
                    text "[Rede1_Erkenntnis3]"
                else:
                    text "[Rede1_Aufruf3]"
        action[
            Function(Decisions.__setitem__,which_decision - 1, 3),
            SetVariable("Aggression", Aggression-1),
            SetVariable("Which_decision", which_decision+1),
            #Jump(expression="Decision_stage_"+str(which_decision))
        ]

    button:
        xpos 800
        ypos 700
        frame:
            xpadding 15                                                                 
            ypadding 15                                                                 
            add "UI/paper.png":
                xsize Box_option_image_width
                ysize Box_option_image_height
                xalign 0.5
                yalign 0.5
            xsize Box_option_width
            ysize Box_option_height                                                  
            vbox:                                                                                                                         
                xalign 0.5                                                                  
                yalign 0.5
                if which_decision==1:
                    text "[Rede1_Einstieg4]"
                elif which_decision==2:
                    text "[Rede1_Reaktion4]"
                elif which_decision==3:
                    text "[Rede1_Hinführung4]"
                elif which_decision==4:
                    text "[Rede1_Problem4]"
                elif which_decision==5:
                    text "[Rede1_Erkenntnis4]"
                else:
                    text "[Rede1_Aufruf4]"
        action[
            Function(Decisions.__setitem__,which_decision - 1, 4),
            SetVariable("Aggression", Aggression-2),
            SetVariable("Which_decision", which_decision+1),
            Jump(expression="Decision_stage_"+str(which_decision))
        ]





style Decision_UI_text:
    size 20
    color"#524e44" 