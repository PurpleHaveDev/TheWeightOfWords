screen mainmenu:
    style_prefix "MenuDE"

    frame:
        background None
        xalign 0.5
        yalign 0.5               
        add "UI/TitleScreen.png":
            xsize 2560
            ysize 1440

    imagebutton:
        xalign 0.14
        yalign 0.5  
        idle "UI/Btn_Start_idle.png"
        hover "UI/Btn_Start_hover.png"
        focus_mask True
        action[
            Jump ("Game_Start")
        ]

    imagebutton:
        xalign 0.14
        yalign 0.5  
        idle "UI/Btn_Optionen_idle.png"
        hover "UI/Btn_Optionen_hover.png"
        focus_mask True
        action[
            NullAction()
        ]

    imagebutton:
        xalign 0.14
        yalign 0.5  
        idle "UI/Btn_Entwickler_idle.png"
        hover "UI/Btn_Entwickler_hover.png"
        focus_mask True
        action[
            NullAction()
        ]

screen Szenarios:
    style_prefix "ScenariosDE"
    
    frame:
        background None
        xalign 0.5
        yalign 0.5               
        add "UI/Table_bg.png":
            xsize 2560
            ysize 1440

    imagebutton:  
        idle "UI/Sz1_idle.png"
        hover "UI/Sz1_hover.png"
        focus_mask True
        action[
            SetVariable("Szenario",1),
            SetVariable("Aggression",0),
            SetVariable("Decisions",[0,0,0,0,0,0]),
            Jump ("Szenario1")           
        ]
    frame:
        background None
        vbox:
            xpos 150
            ypos 150
            xsize 600
            text "{color=#000}Szenario 1: Der Anschlag"
            text ""
            text "{size=*0.8}{color=#000}Auf dem Siegesplatz explodieren mehrere Sprengsätze. 539 Menschen sterben, viele werden noch vermisst. Das Land steht unter Schock. Du bist die Präsidentin und musst zur Nation sprechen. Finde die richtigen Worte, Absatz für Absatz, und entscheide, wie du das Land durch diesen schwierigen Moment führst."

    imagebutton:  
        idle "UI/Sz2_idle.png"
        hover "UI/Sz2_hover.png"
        focus_mask True
        action[
            SetVariable("Szenario",2),
            SetVariable("Aggression",0),
            SetVariable("Decisions",[0,0,0,0,0,0]),
            NullAction()
        ]
    frame:
        background None
        vbox:
            xpos 950
            ypos 150
            xsize 600
            text "{color=#000}Szenario 2: Die Nordbankkrise"
            text ""
            text "{size=*0.8}{color=#000}Eine große Bank muss Insolvenz anmelden. Die Börsen stürzen ab, die Menschen haben Angst um ihr Geld und ihre Rücklagen. Du bist die Präsidentin und musst der Nation erklären, wie es jetzt weitergeht. Finde die richtigen Worte, Absatz für Absatz, und entscheide, wie du das Land durch die Krise führst. (Coming Soon)"

    imagebutton:  
        idle "UI/Sz3_idle.png"
        hover "UI/Sz3_hover.png"
        focus_mask True
        action[
            SetVariable("Szenario",3),
            SetVariable("Aggression",0),
            SetVariable("Decisions",[0,0,0,0,0,0]),
            NullAction()
        ]


$Szenario = 1
$Aggression = 0
$Decisions= [0,0,0,0,0,0]
jump Szenario1