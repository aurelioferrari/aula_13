#ler o ano de nascimento de sete pessoas e mostrar quantas ainda são menores de idade

from datetime import date

ano1 = int(input("Qual o ano de nascimento? "))
ano2 = int(input("Qual o ano de nascimento? "))
ano3 = int(input("Qual o ano de nascimento? "))
ano4 = int(input("Qual o ano de nascimento? "))
ano5 = int(input("Qual o ano de nascimento? "))
ano6 = int(input("Qual o ano de nascimento? "))
ano7 = int(input("Qual o ano de nascimento? "))

atual = date.today().year

idade1 = atual - ano1
idade2 = atual - ano2
idade3 = atual - ano3
idade4 = atual - ano4
idade5 = atual - ano5
idade6 = atual - ano6
idade7 = atual - ano7

total = 0

lista = [idade1, idade2, idade3, idade4, idade5, idade6, idade7]
for c in range(0, 7):
    idade = lista[c]
    if idade < 18:
        total = total + 1

print("{} pessoas são menores de idade.".format(total))


