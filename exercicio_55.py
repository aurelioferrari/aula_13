# ler o peso de 5 pessoas e mostrar o maior e menor peso
lista = []

for c in range(1,6):
    peso = float(input("Qual o peso da {}ª pessoa? "))
    lista.append(peso)

lista.sort()
print("O maior peso foi: {:.2f}".format(lista[4]))
print("O menor peso foi: {:.2f}".format(lista[0]))