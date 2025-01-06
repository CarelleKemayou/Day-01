#Exo5
def liste_inversee():
    Liste=[]
    Liste_inverse=[]
    Nombre_elements=int(input("Entrez le nombre d'elements que vous voulez: "))
    if Nombre_elements:
        for n in range (Nombre_elements):
            elements=input("entrez  l'element a ajouter")
            Liste.append(elements)
        print("Votre liste est",Liste)
        for m in range(1,len(Liste)+1):
            m=-1*m
            Liste_inverse.append(Liste[m])
        print("Votre liste inversée est",Liste_inverse)
    else:
        print("mettez un nombre valide")
liste_inversee()