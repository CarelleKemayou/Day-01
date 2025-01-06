#Exo7
def Voyelles():
    Phrase=str(input("Entrez une phrase"))
    if Phrase:
        somme=0
        for n in Phrase:
            if n in ["a","e","i","o","u","é","è","ê"]:
               somme+=1
        print("la phrase"f"{Phrase} a {somme} voyelles")
    else:
        print("mettez une phrase/mot valide")
Voyelles()