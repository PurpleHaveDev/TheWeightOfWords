screen Scenario1_Intro:
    style_prefix "Intro_UI"

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
            Jump ("Newspaper")
        ]

    imagebutton:
        xalign 0.5
        yalign 0.5  
        idle "UI/Geheimakte_idle.png"
        hover "UI/Geheimakte_hover.png"
        at Transform(zoom=1.32)
        focus_mask True
        action[
            Jump ("Geheimakte")
        ]
 
    imagebutton:
        xalign 0.2
        yalign 0.5  
        idle "UI/Handy_idle.png"
        hover "UI/Handy_hover.png"
        at Transform(zoom=1.32)
        focus_mask True
        action[
            Jump ("Smartphone")
        ]
 

 
 
    button:
        xpos 400
        ypos 1200
        frame:
            xalign 0.5
            yalign 0.5
            vbox:
                text "Auf zur Rede"
        action(
            Jump ("Tutorial")
        )

#77777777777777777777777777777777777777777777777777777777777777777777777777777777777
 
label Geheimakte:
    call screen Classified_Data

screen Classified_Data:
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

label Smartphone:
    call screen Sc_Smartphone

screen Sc_Smartphone:
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

label Newspaper:
    call screen Sc_Newspaper

screen Sc_Newspaper:
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
            text " ^ "
        action[
            SetVariable ("Zeitungshöhe",Zeitungshöhe+100)
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
            text "V"
        action[
            SetVariable ("Zeitungshöhe",Zeitungshöhe-100)
        ] 

