screen Rede_Menu_Style:

    style_prefix "Decision_UI"

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
            #grid 2 3:                          # vbox and hbox for vertical and horizontally aligned text respectively
                                                # use (grid "width" "height":) for combined hbox and vbox aka. a Grid
            vbox:
                xalign 0.5
                yalign 0.5
                text "[Rede1_Einstieg1]"
            action SetVariable("Decision_1",[1,0,0,0])
            action jump ("Descision_stage_1")
        
    button:
        xpadding 15               
        ypadding 15               
        #add Solid ("#b1a688")
        add "UI/paper.png":
            xsize Box_option_image_width
            ysize Box_option_image_height
            xalign 0.5
            yalign 0.5
        xpos 800
        ypos 100
        xsize Box_option_width
        ysize Box_option_height

        vbox:
            xalign 0.5
            yalign 0.5
            text "[Rede1_Einstieg2]"




    button:
        xpadding 15               
        ypadding 15               
        #add Solid ("#b1a688")
        add "UI/paper.png":
            xsize Box_option_image_width
            ysize Box_option_image_height
            xalign 0.5
            yalign 0.5
        xpos 200
        ypos 700
        xsize Box_option_width
        ysize Box_option_height
                         
        vbox:
            xalign 0.5
            yalign 0.5
            text "[Rede1_Einstieg3]"




    button:
        xpadding 15               
        ypadding 15               
        #add Solid ("#b1a688")
        add "UI/paper.png":
            xsize Box_option_image_width
            ysize Box_option_image_height
            xalign 0.5
            yalign 0.5
        xpos 800
        ypos 700
        xsize Box_option_width
        ysize Box_option_height

        vbox:
            xalign 0.5
            yalign 0.5
            text "[Rede1_Einstieg4]"


        





style Decision_UI_text:
    size 20
    color"#524e44" 