#Exo8
def Nombre_max():
    Liste=[]
    for n in range(4):
        elements=int(input("entrez l'element a ajouter"))
        Liste.append(elements)
    print("La liste est",Liste)
    Element_max=max(Liste)
    print("Le plus grand chiffre est",Element_max)
Nombre_max()