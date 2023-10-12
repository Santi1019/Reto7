n = float(input("Ingrese un un numero que este entre 2 y 50: "))

if 2<= n <= 50:
    for m in range(1, n + 1):
        if n % m == 0:
            print("Sus divisores son: ", m)

        
    


else:
    print ("El numero debe estar entre 2 y 50")
