label Szenario1:
    if English==False:
        NW "Platzhalter Text."                                                                                   #Hier ist das setup des szenarios in Form eines Zeitzungsartikels
        NW "Platzhalter Text.."
        NW "Platzhalter Text..."
        NA "Du musst jetzt eine Rede halten."                                                                   #Anleitung zum kommenden Gameplay
        NA "Wähle Bausteine der Rede aus um deine Zuhörer in eine bestimmte Richtung zu lenken."
        label decision:
            $Box_option_height = 600
            $Box_option_width = 600
            $Box_option_image_width = 500
            $Box_option_image_height = 500
 
            call screen Rede_Menu_Style

            label Decision_stage_1:
                $which_decision += 1
                jump 

            label Decision_stage_2:
            
            label Decision_stage_3:
                                                                    # Als nächstes muss unbedingt ein Variablen Array erstellt werden, das trackt, welche Option gewählt wurde. 
                                                                    # Fragen zu Klären: Wie viele Varianten von Auswirkungen -"Enden"- soll es geben?
                                                                    # Wie soll die immediate Reaktion der audience aussehen?
                                                                    # Wie soll dir finale form der Auswirkungen aussehen? png's, animationen, Text?
                                                                    # Wie können wir den Punkt Hass und Manipulation noch härter heimhämern?                                                                
            # menu:
            #     "[Rede1_Reaktion1]":
            #         AU "*reaktion*"
            #         $Aggression+=2
            #     "[Rede1_Reaktion2]":
            #         AU "*reaktion*"
            #         $Aggression+=1
            #     "[Rede1_Reaktion3]":
            #         AU "*reaktion*"
            #         $Aggression-=1
            #     "[Rede1_Reaktion4]":
            #         AU "*reaktion*"
            #         $Aggression-=2

            # menu:
            #     "[Rede1_Hinführung1]":
            #         AU "*reaktion*"
            #         $Aggression+=2
            #     "[Rede1_Hinführung2]":
            #         AU "*reaktion*"
            #         $Aggression+=1
            #     "[Rede1_Hinführung3]":
            #         AU "*reaktion*"
            #         $Aggression-=1
            #     "[Rede1_Hinführung4]":
            #         AU "*reaktion*"
            #         $Aggression-=2

            # menu:
            #     "[Rede1_Problem1]":
            #         AU "*reaktion*"
            #         $Aggression+=2
            #     "[Rede1_Problem2]":
            #         AU "*reaktion*"
            #         $Aggression+=1
            #     "[Rede1_Problem3]":
            #         AU "*reaktion*"
            #         $Aggression-=1
            #     "[Rede1_Problem4]":
            #         AU "*reaktion*"
            #         $Aggression-=2

            # menu:
            #     "[Rede1_Erkenntnis1]":
            #         AU "*reaktion*"
            #         $Aggression+=2
            #     "[Rede1_Erkenntnis2]":
            #         AU "*reaktion*"
            #         $Aggression+=1
            #     "[Rede1_Erkenntnis3]":
            #         AU "*reaktion*"
            #         $Aggression-=1
            #     "[Rede1_Erkenntnis4]":
            #         AU "*reaktion*"
            #         $Aggression-=2

            # menu:
            #     "[Rede1_Aufruf1]":
            #         AU "*reaktion*"
            #         $Aggression+=2
            #     "[Rede1_Aufruf2]":
            #         AU "*reaktion*"
            #         $Aggression+=1
            #     "[Rede1_Aufruf3]":
            #         AU "*reaktion*"
            #         $Aggression-=1
            #     "[Rede1_Aufruf4]":
            #         AU "*reaktion*"
            #         $Aggression-=2

                    
            NA "Sieh nun die Auswirkungen deiner Rede auf die Sachlage."                
            NW "Platzhalter Text."
            NW "Platzhalter Text.."
            NW "Platzhalter Text..."
            jump start  


                    # Und jz das ganze nommal auf englisch


    else:
        NW "Sample Text."                                                                                                            #Hier ist das setup des szenarios in Form eines Zeitzungsartikels
        NW "Sample Text.."
        NW "Sample Text..."
        NA "You have to deliver a speech."                                                                                          #Anleitung zum kommenden Gameplay
        NA "Choose a component to construct your speech. Choose carefully to steer your audience into a favorable direction."

        menu:
            "[Rede1_Einstieg1E]":
                AU "*reaktion*"
                $Aggression+=2
            "[Rede1_Einstieg2E]":
                AU "*reaktion*"
                $Aggression+=1
            "[Rede1_Einstieg3E]":
                AU "*reaktion*"
                $Aggression-=1
            "[Rede1_Einstieg4E]":
                AU "*reaktion*"
                $Aggression-=2

        menu:
            "[Rede1_Reaktion1E]":
                AU "*reaktion*"
                $Aggression+=2
            "[Rede1_Reaktion2E]":
                AU "*reaktion*"
                $Aggression+=1
            "[Rede1_Reaktion3E]":
                AU "*reaktion*"
                $Aggression-=1
            "[Rede1_Reaktion4E]":
                AU "*reaktion*"
                $Aggression-=2

        menu:
            "[Rede1_Hinführung1E]":
                AU "*reaktion*"
                $Aggression+=2
            "[Rede1_Hinführung2E]":
                AU "*reaktion*"
                $Aggression+=1
            "[Rede1_Hinführung3E]":
                AU "*reaktion*"
                $Aggression-=1
            "[Rede1_Hinführung4E]":
                AU "*reaktion*"
                $Aggression-=2

        menu:
            "[Rede1_Problem1E]":
                AU "*reaktion*"
                $Aggression+=2
            "[Rede1_Problem2E]":
                AU "*reaktion*"
                $Aggression+=1
            "[Rede1_Problem3E]":
                AU "*reaktion*"
                $Aggression-=1
            "[Rede1_Problem4E]":
                AU "*reaktion*"
                $Aggression-=2

        menu:
            "[Rede1_Erkenntnis1E]":
                AU "*reaktion*"
                $Aggression+=2
            "[Rede1_Erkenntnis2E]":
                AU "*reaktion*"
                $Aggression+=1
            "[Rede1_Erkenntnis3E]":
                AU "*reaktion*"
                $Aggression-=1
            "[Rede1_Erkenntnis4E]":
                AU "*reaktion*"
                $Aggression-=2

        menu:
            "[Rede1_Aufruf1E]":
                AU "*reaktion*"
                $Aggression+=2
            "[Rede1_Aufruf2E]":
                AU "*reaktion*"
                $Aggression+=1
            "[Rede1_Aufruf3E]":
                AU "*reaktion*"
                $Aggression-=1
            "[Rede1_Aufruf4E]":
                AU "*reaktion*"
                $Aggression-=2

        NA "Check out the reprecussions your speech had on the current situation."
        NW "Sample Text."
        NW "Sample Text.."
        NW "Sample Text..."
        jump start