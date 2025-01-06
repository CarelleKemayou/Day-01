#Exo 6
def Devinette():
    Nombre_genere=randint(1,100)
    print("Vous allez essayer de deviner un chiffre aleatoire entre 1 et 100")
    Reponse=False
    while Reponse==False:
        choix = int(input("Entrez un chiffre"))
        if choix:

            if choix >Nombre_genere:
                print("plus bas")
            if choix <Nombre_genere:
                print("plus haut")
            if choix == Nombre_genere:
                print(f"Vous avez deviné!Le chiffre était {Nombre_genere}")
                Reponse==True
        else:
            print("mettez un nombre valide")
Devinette()