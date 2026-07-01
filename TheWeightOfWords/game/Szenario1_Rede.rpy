
if English==False:
    label Szenario1:
        NW "(Debug)Setup:"     
        call screen Scenario_Intro                                                                        #Hier ist das setup des szenarios in Form eines Zeitzungsartikels
        NW "(hier wäre jetzt ein Bild von der Zeitung, die den Anschlag beschreibt)"
        NW "539 Tote bei Anschlag auf die Hauptstadt. Bevölkerung in Schockstarre. Regierung unter Druck."


    label Tutorial:
        NA "Du musst jetzt eine Rede halten."                                                                   #Anleitung zum kommenden Gameplay
        NA "Wähle Bausteine der Rede aus um deine Zuhörer in eine bestimmte Richtung zu lenken."

    label Decision:
        $Box_option_height = 600
        $Box_option_width = 600
        $Box_option_image_width = 900
        $Box_option_image_height = 500
        $Decision1 = True
 
        call screen Rede_Menu_Style


    label Decision_stage_1:
        $which_decision = which_decision+1
        $Function(renpy.notify, "Das klappt")
        while Decision1==True:
            if Decisions[0]==1:
                $Speech[0] = Rede1_Einstieg1
                $Decision1 = False 
            elif Decisions[0]==2:
                $Speech[0] = Rede1_Einstieg2
                $Decision1 = False 
            elif Decisions[0]==3:
                $Speech[0] = Rede1_Einstieg3
                $Decision1 = False 
            elif Decisions[0]==4:
                $Speech[0] = Rede1_Einstieg4
                $Decision1 = False 
            else:
                pass
        $Decision2 = True
        jump Decision

    label Decision_stage_2:
        $which_decision = which_decision+1        
        $Function(renpy.notify, "Das klappt2")
        while Decision2==True:
            if Decisions[1]==1:
                $Speech[1] = Rede1_Reaktion1
                $Decision2 = False
            elif Decisions[1]==2:
                $Speech[1] = Rede1_Reaktion2
                $Decision2 = False
            elif Decisions[1]==3:
                $Speech[1] = Rede1_Reaktion3
                $Decision2 = False
            elif Decisions[1]==4:
                $Speech[1] = Rede1_Reaktion4
                $Decision2 = False
            else:
                pass
        $Decision3 = True
        jump Decision
    
    label Decision_stage_3:
        $which_decision = which_decision+1
        $Function(renpy.notify, "Das klappt3")
        while Decision3==True:
            if Decisions[2]==1:
                $Speech[2] = Rede1_Hinfuehrung1
                $Decision3 = False 
            elif Decisions[2]==2:
                $Speech[2] = Rede1_Hinfuehrung2
                $Decision3 = False 
            elif Decisions[2]==3:
                $Speech[2] = Rede1_Hinfuehrung3
                $Decision3 = False 
            elif Decisions[2]==4:
                $Speech[2] = Rede1_Hinfuehrung4
                $Decision3 = False 
            else:
                pass
        $Decision4 = True
        jump Decision

    label Decision_stage_4:
        $which_decision = which_decision+1        
        $Function(renpy.notify, "Das klappt4")
        while Decision4==True:
            if Decisions[3]==1:
                $Speech[3] = Rede1_Problem1
                $Decision4 = False 
            elif Decisions[3]==2:
                $Speech[3] = Rede1_Problem2
                $Decision4 = False 
            elif Decisions[3]==3:
                $Speech[3] = Rede1_Problem3
                $Decision4 = False
            elif Decisions[3]==4:
                $Speech[3] = Rede1_Problem4
                $Decision4 = False 
            else:
                pass
        $Decision5 = True
        jump Decision

    label Decision_stage_5:
        $which_decision = which_decision+1
        $Function(renpy.notify, "Das klappt5")
        while Decision5==True:
            if Decisions[4]==1:
                $Speech[4] = Rede1_Erkenntnis1
                $Decision5 = False 
            elif Decisions[4]==2:
                $Speech[4] = Rede1_Erkenntnis2
                $Decision5 = False 
            elif Decisions[4]==3:
                $Speech[4] = Rede1_Erkenntnis3
                $Decision5 = False 
            elif Decisions[4]==4:
                $Speech[4] = Rede1_Erkenntnis4
                $Decision5 = False 
            else:
                pass
        $Decision6 = True
        jump Decision

    label Decision_stage_6:
        $which_decision = which_decision+1
        $Function(renpy.notify, "Das klappt6")
        while Decision6==True:
            if Decisions[5]==1:
                $Speech[5] = Rede1_Aufruf1
                $Decision6 = False
            elif Decisions[5]==2:
                $Speech[5] = Rede1_Aufruf2
                $Decision6 = False
            elif Decisions[5]==3:
                $Speech[5] = Rede1_Aufruf3
                $Decision6 = False
            elif Decisions[5]==4:
                $Speech[5] = Rede1_Aufruf4
                $Decision6 = False

            else:
                pass
        jump Decision
        
                                                                    # Als nächstes muss unbedingt ein Variablen Array erstellt werden, das trackt, welche Option gewählt wurde. 
                                                                    # Fragen zu Klären: Wie viele Varianten von Auswirkungen -"Enden"- soll es geben?
                                                                    # Wie soll die immediate Reaktion der audience aussehen?
                                                                    # Wie soll dir finale form der Auswirkungen aussehen? png's, animationen, Text?
                                                                    # Wie können wir den Punkt Hass und Manipulation noch härter heimhämern?                                                               

    label Decision_stage_7:                
        NA "Sieh nun die Auswirkungen deiner Rede auf die Sachlage."      
        if Aggression >= 7:
            NA "Das Kabinett erklärte den Nachbarstaaten wenige Tage nach dem Anschlag den Krieg. Was eine kurze militärische Reaktion auf den Terror sein sollte, wurde zu einem Konflikt, der die Region für Generationen prägte. Die Bevölkerung war zunächst geeint."
            NA "Aber je länger der Krieg andauerte, desto tiefer wurden die Risse. Die Wirtschaft brach unter den Kriegskosten ein. Verfolgung und Hass fraßen sich durch die Gesellschaft."
            NA "In der Forschung gilt die Rede vom Siegesplatz als der Wendepunkt, an dem der Weg in diesen Krieg eingeschlagen wurde. Noch heute, Jahrzehnte später, ist das Land gespalten."
            NA "Immer wieder aufkeimende Konflikte, Gewalt und Misstrauen definieren Politik und Gesellschaft."
        elif Aggression >=1 and Aggression <=6:
            NA "Die Ermittlungen nach dem Anschlag führten zu Verhaftungen. Die Netzwerke hinter dem Attentat wurden zerschlagen. Das Vertrauen in den Staat stieg – in großen Teilen der Bevölkerung. Das gemeinsame Feindbild half, die Reihen zu schließen."
            NA "Doch die verschärften Sicherheitsmaßnahmen der folgenden Jahre hatten ihren Preis. Minderheiten und Migranten aus den Nachbarländern gerieten immer wieder unter Verdacht. "
            NA "Heftige Debatten über Ausgrenzung, Rassismus und Diskriminierung prägten das Land noch auf Jahre. Das Land hielt dennoch zusammen."
            NA "Es behauptete sich gegen extremistische Kräfte im In- und Ausland. Ob dieser Zusammenhalt trotz der Ausgrenzung gelang oder wegen ihr, darüber streitet die Forschung bis heute."
            NA "Die Rede vom Siegesplatz gilt als Ausgangspunkt für diesen kämpferischen Weg, der jedoch gesellschaftlich umstritten ist."
        elif Aggression >=-6 and Aggression <=0:
            NA "Die gesellschaftliche Spaltung, die die Täter beabsichtigt hatten, blieb aus. Das Land rang öffentlich um den richtigen Umgang mit Trauer, Sicherheit und Zusammenhalt – "
            NA "in Parlamentsdebatten, in Zeitungen, im Alltag an der Kaffeemaschine. Dieser Streit verlangsamte Entscheidungen."
            NA "Er hielt das Land aber auch zusammen. Aus oppositionellen Kreisen wurde der Präsidentin nach ihrer Rede immer wieder Schwäche vorgehalten."
            NA "Diese Gruppe blieb in der Minderheit – bestimmte aber lautstark die Debatten."
            NA "Die Rede vom Siegesplatz gilt als Ausgangspunkt für den zähen, manchmal lähmenden, aber letztlich tragfähigen Weg, den das Land nach dem Anschlag ging."
        else:
            NA "In den Monaten nach dem Anschlag schoben die politischen Lager einander die Verantwortung zu. Eine klare Linie blieb aus. Die Präsidentin überstand ein Misstrauensvotum nicht."
            NA "Das Vertrauen in die Institutionen sank schleichend, aber stetig. Die Wirtschaft stagnierte. Drei Kabinette scheiterten in drei Jahren."
            NA "Seitdem wechselten Minderheitsregierungen einander ab. Kaum eine politische Kraft schafft es noch, das Land hinter sich zu vereinen."
            NA "Die fehlenden Konsequenzen nach dem ersten Anschlag hatten einen Preis: Zwei weitere Attentate erschütterten das Land keine fünf Jahre später."
            NA "Das Land rutschte in eine Phase der Unruhen und Ausschreitungen ab, aus der es bis heute nicht herausgefunden hat. Immer wieder aufflammende Bürgerkriege prägen Alltag und Politik."
            NA "Dass in der Rede auf dem Siegesplatz kein klarer Pfad eingeschlagen wurde, gilt unter Historikern heute als Ausgangspunkt für den Niedergang."
            


        
        $Szenario = 1
        $Szenario = 1
        $Aggression = 0
        $Decisions= [0,0,0,0,0,0] 
        $which_decision= 1
        $Speech = ["...","...","...","...","...","..."]
        jump start  


                    # Und jz das ganze nommal auf englisch


else:
    pass