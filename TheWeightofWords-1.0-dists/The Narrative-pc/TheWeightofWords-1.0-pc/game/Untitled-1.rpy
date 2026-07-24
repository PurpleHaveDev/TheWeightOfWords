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
            Jump ("Credits")
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
            Jump ("Szenario2")
        ]
    frame:
        background None
        vbox:
            xpos 950
            ypos 150
            xsize 600
            text "{color=#000}Szenario 2: Die Nordbankkrise"
            text ""
            text "{size=*0.8}{color=#000}Eine große Bank muss Insolvenz anmelden. Die Börsen stürzen ab, die Menschen haben Angst um ihr Geld und ihre Rücklagen. Du bist die Präsidentin und musst der Nation erklären, wie es jetzt weitergeht. Finde die richtigen Worte, Absatz für Absatz, und entscheide, wie du das Land durch die Krise führst."

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
    frame:
        background None
        vbox:
            xpos 1750
            ypos 150
            xsize 600
            text "{color=#000}Szenario 3: Bald verfügbar"


label Credits:
    call screen CreditsDE

screen CreditsDE:
    style_prefix "CreditsDE"
    
    frame:
        background None
        xalign 0.5
        yalign 0.5               
        add "UI/Table_bg.png":
            xsize 2560
            ysize 1440

    frame:
        xsize 800
        ysize 1100
        xalign .5
        yalign .5
        vbox:
            xalign .5
            yalign .5
            text "{size=*2}{color=#F2AE29}    Das Narrativ"
            text ""
            text"{size=*1.5}{color=#DEDDAF}              Idee:"
            text"{size=*1.8}{color=#f1f0be}      Nora Varga"
            text""
            text"{size=*1.5}{color=#DEDDAF}            Writing:"
            text"{size=*1.8}{color=#f1f0be}      Nora Varga" 
            text""
            text"{size=*1.5}{color=#DEDDAF} Graphiken und 2D Art:"
            text"{size=*1.8}{color=#f1f0be}     Miriam Löffler"
            text""
            text"{size=*1.5}{color=#DEDDAF}    Programmierung:"
            text"{size=*1.8}{color=#f1f0be}      Philipp Lüer"
                  
    button:
        xpos 100
        ypos 1200
        frame:
            xalign 0.5
            yalign 0.5
            vbox:
                text "<<< zurück"
        action Jump ("start")