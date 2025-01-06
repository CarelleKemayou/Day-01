def Factoriel():
    Nombre= int(input("Entrez le nombre: "))
    if Nombre==0:
        Nombre=1
        print(f"0!={Nombre}")
    else:
        Factor = 1
        for Chiffre in range(2, Nombre+1):
            Factor=Factor*Chiffre
        print(f"{Nombre}! = {Factor}")
Factoriel()