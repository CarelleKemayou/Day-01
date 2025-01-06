from random import randint


def Devinettes_lim_1000():
    Nombre_genere=randint(1,1000)
    print(Nombre_genere)
    print("Vous allez essayer de deviner un chiffre aleatoire entre 1 et 100")
    Reponse=False
    i=10
    j=0
    while Reponse==False or i==0:
        choix = int(input("Entrez un chiffre"))
        if choix:

            if choix >Nombre_genere:
                print(f"plus bas,il reste {i} essai")
                i-=1
                j+=1
            if choix <Nombre_genere:
                print(f"plus haut,il reste {i} essai")
                i -= 1
                j += 1
            if choix == Nombre_genere:
                print(f"Vous avez deviné!Le chiffre était {Nombre_genere} en {j} essais")
                Reponse==True
        else:
            print("mettez un nombre valide")
    print(f"Vous n'avez pas reussi le chiffre était {Nombre_genere}")
Devinettes_lim_1000()