# The script of the game goes in this file.
#this is the main file for this game. Any Setup for Characters or Variables pls do in seperate sheets found in rnpy folder.
#Please keep this as organized as possible

label start:

    C "Wähle eine Sprache"
    menu:
        "Deutsch":
            pass
        "English":
            $English=True

if English==False:
    C "Das ist auf Deutsch."

else:
    C "This is in English."

return
