#exo 10
def Notes_moyennes():
    Notes= input("Entrez plusieurs notes séparées par des virgules")
    liste_notes=Notes.split(",")
    somme=0
    for n in liste_notes:
        somme=somme+int(n)
        moyenne=somme/len(liste_notes)
    print("la moyenne des notes misent est de:",moyenne)
Notes_moyennes()