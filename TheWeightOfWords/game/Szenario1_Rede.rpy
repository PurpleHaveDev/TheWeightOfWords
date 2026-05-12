label Szenario1:
    if English==False:
        NW "Platzhalter Text"                                                                                   #Hier ist das setup des szenarios in Form eines Zeitzungsartikels
        NW "Platzhalter Text"
        NW "Platzhalter Text"
        NA "Du musst jetzt eine Rede halten."                                                                   #Anleitung zum kommenden Gameplay
        NA "Wähle Bausteine der Rede aus um deine Zuhörer in eine bestimmte Richtung zu lenken."    
        menu:
            "[Rede1Einleitung1]":
                AU "*reaktion*"
            "[Rede1Einleitung2]":
                AU "*reaktion*"
            "[Rede1Einleitung3]":
                AU "*reaktion*"
            "[Rede1Einleitung4]":
                AU "*reaktion*"

        menu:
            "[Rede1_Thema1]":
                AU "*reaktion*"
            "[Rede1_Thema2]":
                AU "*reaktion*"
            "[Rede1_Thema3]":
                AU "*reaktion*"
            "[Rede1_Thema4]":
                AU "*reaktion*"

        menu:
            "[Rede1_Problem1]":
                AU "*reaktion*"
            "[Rede1_Problem2]":
                AU "*reaktion*"
            "[Rede1_Problem3]":
                AU "*reaktion*"
            "[Rede1_Problem4]":
                AU "*reaktion*"

        menu:
            "[Rede1_Lösung1]":
                AU "*reaktion*"
            "[Rede1_Lösung2]":
                AU "*reaktion*"
            "[Rede1_Lösung3]":
                AU "*reaktion*"
            "[Rede1_Lösung4]":
                AU "*reaktion*"

        menu:
            "[Rede1_Zukunft1]":
                AU "*reaktion*"
            "[Rede1_Zukunft2]":
                AU "*reaktion*"
            "[Rede1_Zukunft3]":
                AU "*reaktion*"
            "[Rede1_Zukunft4]":
                AU "*reaktion*"

    NA "Sieh nun die Auswirkungen deiner Rede auf die Sachlage."
    NW "Platzhalter Text"
    NW "Platzhalter Text"

    else:
        NW "Sample Text"                                                                                                     #Hier ist das setup des szenarios in Form eines Zeitzungsartikels
        NW "Smaple Text"
        NW "Sample Text"
        NA "You have to deliver a speech."                                                                                   #Anleitung zum kommenden Gameplay
        NA "Choose a component to construct your speech. Choose carefully to steer your audience into a favorable."
        menu:
            "[Rede1Einleitung1E]":
                AU "*reaktion*"
            "[Rede1Einleitung2E]":
                AU "*reaktion*"
            "[Rede1Einleitung3E]":
                AU "*reaktion*"
            "[Rede1Einleitung4E]":
                AU "*reaktion*"

        menu:
            "[Rede1_Thema1E]":
                AU "*reaktion*"
            "[Rede1_Thema2E]":
                AU "*reaktion*"
            "[Rede1_Thema3E]":
                AU "*reaktion*"
            "[Rede1_Thema4E]":
                AU "*reaktion*"

        menu:
            "[Rede1_Problem1E]":
                AU "*reaktion*"
            "[Rede1_Problem2E]":
                AU "*reaktion*"
            "[Rede1_Problem3E]":
                AU "*reaktion*"
            "[Rede1_Problem4E]":
                AU "*reaktion*"

        menu:
            "[Rede1_Lösung1E]":
                AU "*reaktion*"
            "[Rede1_Lösung2E]":
                AU "*reaktion*"
            "[Rede1_Lösung3E]":
                AU "*reaktion*"
            "[Rede1_Lösung4E]":
                AU "*reaktion*"

        menu:
            "[Rede1_Zukunft1E]":
                AU "*reaktion*"
            "[Rede1_Zukunft2E]":
                AU "*reaktion*"
            "[Rede1_Zukunft3E]":
                AU "*reaktion*"
            "[Rede1_Zukunft4E]":
                AU "*reaktion*"

        NA "Check out the reprecussions your speech had on the current situation."
        NW "Sample Text"
        NW "Sample Text"
