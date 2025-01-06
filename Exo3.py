#Exo 3
def conversion():
    D_celcius=int(input("Entrez la tenperature en degrées celsius"))
    if D_celcius:
        Absolute_Temp=-273.16
        if D_celcius > Absolute_Temp:
            D_Fahrenheit=(D_celcius * 9/5) + 32
            print(f"La temperature en Fahrenheit est de {D_Fahrenheit}°F")
        else:
            print(f"cette temperature est en dessous de la temperature{Absolute_Temp}°C et est impossible a obtenir entrez de nouvelle valeurs")
    else:
        print("Entrez une temperature valide")
conversion()