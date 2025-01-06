#Exo 9
def palindrome():
    Phrase = str(input("Entrez une phrase"))
    if Phrase==Phrase[::-1]:
        print(f"le mot {Phrase} est un palindrome")
    else:
        print(f"le mot {Phrase} n'est pas un palindrome")
palindrome()