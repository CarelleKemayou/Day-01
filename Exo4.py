#Exo 4
def Table_de_multiplication():
    Chiffre=int(input("Quelle est le chiffre dont vous voulez la table:"))
    Table=10
    if Chiffre:
        print(f"La table de {Chiffre} est:")
        for n in range(Table+1):
            Produit=Chiffre*n
            print(f"{Chiffre} x {n} = {Produit} ")

    else:
        print("Entrez invalide")
Table_de_multiplication()