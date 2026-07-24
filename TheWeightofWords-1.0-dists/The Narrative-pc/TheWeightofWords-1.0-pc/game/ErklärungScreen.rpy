label Sp1_Erklärung:
    call screen Sp1_ErklärungScreen

screen Sp1_ErklärungScreen: 
    style_prefix "Sp1_Diagramm"

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
                Jump ("Sp1_Erklärung")
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
                SetVariable("Speech1", ["","","","","",""]),
                SetVariable("Auswirkung", ["","","","","",""]),
                Jump ("start")
            )



        vbox:
            xpos 300
            ypos 200
            xsize 500
            text Speech1[0]:
                #size 30
                color "#000"             
        vbox:
            xpos 1050
            ypos 200
            xsize 500
            text Speech1[1]:
                #size 30
                color "#000"
        vbox:
            xpos 1790
            ypos 200
            xsize 500
            text Speech1[2]:
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
            text Speech1[3]:
                #size 30
                color "#000"             
        vbox:
            xpos 1050
            ypos 200
            xsize 500
            text Speech1[4]:
                #size 30
                color "#000"
        vbox:
            xpos 1790
            ypos 200
            xsize 500
            text Speech1[5]:
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
                SetVariable("Speech1", ["","","","","",""]),
                SetVariable("Auswirkung", ["","","","","",""]),
                Jump ("start")
            )

