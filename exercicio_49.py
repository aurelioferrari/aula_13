# tabuada de um número

numero = int(input("digite o número da tabuada: "))
for c in range(1, 11):
    multi = numero * c
    print("{} x {} = {}".format(numero, c, multi))