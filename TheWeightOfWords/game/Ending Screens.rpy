#Ending Screens

screen Ending_1o1_Aggresive:
    style_prefix "end1"

    frame:
        background None
        xalign 0.5
        yalign 0.5
        add "UI/End_Aggressiv.png":
            xsize 2560
            ysize 1440
        vbox:
            xpos 1550
            ypos 180
            xsize 800
            text "{size=*.8}{color=#000}Das Kabinett erklärte den Nachbarstaaten wenige Tage nach dem Anschlag den Krieg. Was eine kurze militärische Reaktion auf den Terror sein sollte, wurde zu einem Konflikt, der die Region für Generationen prägte. Die Bevölkerung war zunächst geeint."
            text "{size=*.8}{color=#000}Aber je länger der Krieg andauerte, desto tiefer wurden die Risse. Die Wirtschaft brach unter den Kriegskosten ein. Verfolgung und Hass fraßen sich durch die Gesellschaft."
            text "{size=*.8}{color=#000}In der Forschung gilt die Rede vom Siegesplatz als der Wendepunkt, an dem der Weg in diesen Krieg eingeschlagen wurde. Noch heute, Jahrzehnte später, ist das Land gespalten."
            text "{size=*.8}{color=#000}Immer wieder aufkeimende Konflikte, Gewalt und Misstrauen definieren Politik und Gesellschaft."

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
            Jump ("Erklärung")
        )



screen Ending_1o2_Fiesty:
    style_prefix "end2"

    frame:
        background None
        xalign 0.5
        yalign 0.5
        add "UI/End_Kaempferisch.png":
            xsize 2560
            ysize 1440
        vbox:
            xpos 1550
            ypos 180
            xsize 800
            text "{size=*0.87}{color=#000}Die Ermittlungen nach dem Anschlag führten zu Verhaftungen. Die Netzwerke hinter dem Attentat wurden zerschlagen. Das Vertrauen in den Staat stieg – in großen Teilen der Bevölkerung. Das gemeinsame Feindbild half, die Reihen zu schließen."
            text "{size=*0.87}{color=#000}Doch die verschärften Sicherheitsmaßnahmen der folgenden Jahre hatten ihren Preis. Minderheiten und Migranten aus den Nachbarländern gerieten immer wieder unter Verdacht. "
            text "{size=*0.87}{color=#000}Heftige Debatten über Ausgrenzung, Rassismus und Diskriminierung prägten das Land noch auf Jahre. Das Land hielt dennoch zusammen."
            text "{size=*0.87}{color=#000}Es behauptete sich gegen extremistische Kräfte im In- und Ausland. Ob dieser Zusammenhalt trotz der Ausgrenzung gelang oder wegen ihr, darüber streitet die Forschung bis heute."
            text "{size=*0.87}{color=#000}Die Rede vom Siegesplatz gilt als Ausgangspunkt für diesen kämpferischen Weg, der jedoch gesellschaftlich umstritten ist."

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
            Jump ("Erklärung")
        )


screen Ending_1o3_Diplomatic:
    style_prefix "end3"

    frame:
        background None
        xalign 0.5
        yalign 0.5
        add "UI/End_Beschwichtigend.png":
            xsize 2560
            ysize 1440
        vbox:
            xpos 1550
            ypos 180
            xsize 800
            text "{size=*0.9}{color=#000}Die gesellschaftliche Spaltung, die die Täter beabsichtigt hatten, blieb aus. Das Land rang öffentlich um den richtigen Umgang mit Trauer, Sicherheit und Zusammenhalt – "
            text "{size=*0.9}{color=#000}in Parlamentsdebatten, in Zeitungen, im Alltag an der Kaffeemaschine. Dieser Streit verlangsamte Entscheidungen."
            text "{size=*0.9}{color=#000}Er hielt das Land aber auch zusammen. Aus oppositionellen Kreisen wurde der Präsidentin nach ihrer Rede immer wieder Schwäche vorgehalten."
            text "{size=*0.9}{color=#000}Diese Gruppe blieb in der Minderheit – bestimmte aber lautstark die Debatten."
            text "{size=*0.9}{color=#000}Die Rede vom Siegesplatz gilt als Ausgangspunkt für den zähen, manchmal lähmenden, aber letztlich tragfähigen Weg, den das Land nach dem Anschlag ging."

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
            Jump ("Erklärung")
        )



screen Ending_1o4_Calming:
    style_prefix "end4"

    frame:
        background None
        xalign 0.5
        yalign 0.5
        add "UI/End_Versoehnend.png":
            xsize 2560
            ysize 1440
        vbox:
            xpos 1550
            ypos 180
            xsize 800
            text "{size=*0.8}{color=#000}In den Monaten nach dem Anschlag schoben die politischen Lager einander die Verantwortung zu. Eine klare Linie blieb aus. Die Präsidentin überstand ein Misstrauensvotum nicht."
            text "{size=*0.8}{color=#000}Das Vertrauen in die Institutionen sank schleichend, aber stetig. Die Wirtschaft stagnierte. Drei Kabinette scheiterten in drei Jahren."
            text "{size=*0.8}{color=#000}Seitdem wechselten Minderheitsregierungen einander ab. Kaum eine politische Kraft schafft es noch, das Land hinter sich zu vereinen."
            text "{size=*0.8}{color=#000}Die fehlenden Konsequenzen nach dem ersten Anschlag hatten einen Preis: Zwei weitere Attentate erschütterten das Land keine fünf Jahre später."
            text "{size=*0.8}{color=#000}Das Land rutschte in eine Phase der Unruhen und Ausschreitungen ab, aus der es bis heute nicht herausgefunden hat. Immer wieder aufflammende Bürgerkriege prägen Alltag und Politik."
            text "{size=*0.8}{color=#000}Dass in der Rede auf dem Siegesplatz kein klarer Pfad eingeschlagen wurde, gilt unter Historikern heute als Ausgangspunkt für den Niedergang."

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
            Jump ("Erklärung")
        )