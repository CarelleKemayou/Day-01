def Tri():
    Liste = []
    Nombre_elements = int(input("Entrez le nombre d'elements que vous voulez: "))
    if Nombre_elements:
        for n in range(Nombre_elements):
            elements = int(input("entrez  l'element a ajouter"))
            Liste.append(elements)
        print("Votre liste est", Liste)
        liste_Triee=sorted(Liste)
        print("Votre liste triée est",liste_Triee)

Tri()