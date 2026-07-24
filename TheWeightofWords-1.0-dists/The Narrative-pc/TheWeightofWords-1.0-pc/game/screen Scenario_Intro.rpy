screen Scenario1_Intro:
    style_prefix "Sp1_Intro_UI"

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
            Jump ("Sp1_Newspaper")
        ]

    imagebutton:
        xalign 0.5
        yalign 0.5  
        idle "UI/Geheimakte_idle.png"
        hover "UI/Geheimakte_hover.png"
        at Transform(zoom=1.32)
        focus_mask True
        action[
            Jump ("Sp1_Geheimakte")
        ]
 
    imagebutton:
        xalign 0.2
        yalign 0.5  
        idle "UI/Handy_idle.png"
        hover "UI/Handy_hover.png"
        at Transform(zoom=1.32)
        focus_mask True
        action[
            Jump ("Sp1_Smartphone")
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
            Jump ("Sp1_Tutorial")
        )

#77777777777777777777777777777777777777777777777777777777777777777777777777777777777
 
label Sp1_Geheimakte:
    call screen Sp1_Classified_Data

screen Sp1_Classified_Data:
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
        add "UI/Classified.png"       

    button:
        xpos 100
        ypos 1200
        frame:
            xalign 0.5
            yalign 0.5
            vbox:
                text "<<< zurück"
        action Jump ("Szenario1")


#/////////////////////////////////////////////////////////////////////////////////////////

label Sp1_Smartphone:
    call screen Sp1_Sc_Smartphone

screen Sp1_Sc_Smartphone:
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
        add "UI/Twitter.png"       

    button:
        xpos 100
        ypos 1200
        frame:
            xalign 0.5
            yalign 0.5
            vbox:
                text "<<< zurück"
        action Jump ("Szenario1")

#///////////////////////////////////////////////////////////////////////////////

label Sp1_Newspaper:
    call screen Sp1_Sc_Newspaper

screen Sp1_Sc_Newspaper:
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
        background "UI/NWSPaper.png"
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
        action Jump ("Szenario1")

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
            Jump("Sp1_Newspaper")
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
            Jump("Sp1_Newspaper")
        ] 

