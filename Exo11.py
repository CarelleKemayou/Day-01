#exo11
def fizz_buzz():
    for n in range (1,100):
        if n%3==0:
            print("fizz")
        elif n%5==0:
            print("buzz")
        elif n%5==0 and n%3==0:
            print("fizzbuzz")
        else:
            print(n)
fizz_buzz()