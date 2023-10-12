import random

numero_secreto = random.randint(1, 100)

while True:
    
    m = int(input("Adivina el número entre 1 y 100: "))

    if m < numero_secreto:
        print("El número es mayor.")
    elif m > numero_secreto:
        print("El número es menor.")
    else:
        print("Por fin, casi que no caramonda, el numero es: ", numero_secreto)
        break
