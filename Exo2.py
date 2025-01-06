#Exo 2
def Calculatrice():
    Suite=True
    Nombre_1=int(input("Entrez un nombre a ajouter"))
    Nombre_2 = int(input("Entrez l'autre nombre"))
    if Nombre_1 and Nombre_2:
        Operation= str(input("Quelle opération souhaitez vous faire"))
        while Suite==True:
            if Operation not in ["Addition","Soustraction","Multiplication","Division"]:
                print("Cette opération n'est pas permise")
                Operation = str(input("Quelle opération souhaitez vous faire"))
            else:
                if Operation=="Addition":
                    Somme=Nombre_1+Nombre_2
                    print("La somme est",Somme)
                    return Somme
                if Operation=="Soustraction":
                    Difference=Nombre_1-Nombre_2
                    print("La différence est",Difference)
                    return Difference
                if Operation=="Multiplication":
                    Produit=Nombre_1*Nombre_2
                    print("Le produit est",Produit)
                    return Produit
                if Operation=="Division":
                    Quotient=Nombre_1/Nombre_2
                    print("La division donne",Quotient)
                    return Quotient
                Suite=False
    else:
        print("entrée non valide")
Calculatrice()