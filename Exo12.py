from random import randint


def mot_de_passe():
    Longeur=int(input("Entrez la longeur de votre mot de passe: "))

    mot_de_passe=" "
    for n in range(Longeur):
        lettresnum =randint(48, 126)
        lettre=chr(lettresnum)
        mot_de_passe+=lettre
    print("le mot de passe est",mot_de_passe)
mot_de_passe()