screen Scenario_Intro:
    style_prefix "Intro_UI"

    frame:
        background None
        xpadding 15               
        ypadding 15
        xalign 0.5
        yalign 0.5               
        #add Solid ("#eb9e51")
        add "UI/TableOfContents.png":
            xsize 2560
            ysize 1440

    imagebutton:
        idle
        hover
        xpos
        ypos
        action(
            text "Das Klappt"
        )

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



#screen Newspaper_Closeup:
#screen Classified_Data:
#screen Social_Media: