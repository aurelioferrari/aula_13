soma = 0

for c in range(1, 501):
    multiplos = c % 3
    impar = c % 2
    if multiplos == 0 and impar == 1:
        soma = soma + c
print("A soma é: {}".format(soma))
