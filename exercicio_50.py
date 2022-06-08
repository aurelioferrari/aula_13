# ler seis números inteiros e mostrar a soma dos pares

s = 0

for c in range(0, 6):
    numero = int(input("Digite um número: "))
    par = numero % 2
    if par == 0:
        s = s + numero
print("A some é: {}".format(s))