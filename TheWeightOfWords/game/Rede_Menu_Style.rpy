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
            text"[Decision_1]"
            text"[Decision_2]"
            text"[Decision_3]"
            text"[Decision_4]"
            text"[Decision_5]"
            text"[Decision_6]"
            


    button:
        frame:
            xpadding 15               #fügt nen coushion rahmen um den text
            ypadding 15               #ACHTUNG: Das affected nur den Text, nicht den rahmen selbst. Anstatt den rahmen größer zu machen, skaliert es den Text nach innen
            #add Solid ("#b1a688")
            add "UI/paper.png":
                xsize Box_option_image_width
                ysize Box_option_image_height
                xalign 0.5
                yalign 0.5
            xpos 200
            ypos 100
            xsize Box_option_width
            ysize Box_option_height                                                  
            vbox:                                            # vbox and hbox for vertical and horizontally aligned text respectively                                                
                xalign 0.5                                   # use (grid "width" "height":) for combined hbox and vbox aka. a Grid
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
            Function(renpy.notify, "Das klappt"),
            if which_decision==1:
                SetVariable("Decision_1",1)
            elif which_decision==2:
                SetVariable("Decision_2",1)
            elif which_decision==3:
                SetVariable("Decision_3",1)
            elif which_decision==4:
                SetVariable("Decision_4",1)
            elif which_decision==5:
                SetVariable("Decision_5",1)
            else:
                SetVariable("Decision_6",1)

            Jump("Decision_stage_1")
        ]



        

        





style Decision_UI_text:
    size 20
    color"#524e44" 