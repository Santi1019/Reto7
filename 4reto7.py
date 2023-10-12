A = 25
B = 18.9
tasa_a = 0.2
tasa_b = 0.3
edad_xd = 2022

while B <= A:
    A+= A*tasa_a
    B+= B*tasa_b
    edad_xd +=1
print("La poblacion del pais B superará a la del pais A en el año: ", edad_xd)
