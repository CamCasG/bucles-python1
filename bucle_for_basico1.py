#1 imprime todos los números enteros del 0 al 150.
for i in range(151):
    print(i)


#2 imprime todos los múltiplos de 5 entre 5 y 1,000.
for i in range(5,1001):
    if(i%5 == 0):
        print(i)

#3  imprime números enteros del 1 al 100. Si es divisible por 5, imprime "Coding” en su lugar. Si es divisible por 10, imprime "Coding Dojo".
for i in range(1,101):
    if(i%10 == 0):
        print("Coding Dojo")
    elif(i%5== 0):
        print("Coding")
    else:
        print(i)

#4 agrega los enteros impares del 0 al 500,000, e imprime la suma final.
suma = 0
for i in range(0, 500001):
    if(i%2 == 1):
        print(suma)
        suma += i
print(suma) 

#5 imprime números positivos comenzando desde el 2018, en cuenta regresiva de 4 en 4.
for i in range(2018, 0, -4):
    print(i)


#6 establece tres variables: lowNum, highNum, mult. Imprime solo los enteros que sean múltiplos de mult.
lowNum = 4
highNum = 16
mult = 2
for i in range(lowNum, highNum):
    if(i % mult == 0):
        print(i)
