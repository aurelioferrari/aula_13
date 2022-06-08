# ler nome, idade e sexo de 4 pessoas
# média de idade do grupo
# nome do homem mais velho
# quantas mulheres com menos de 20 anos

lista_nome = []
lista_idade = []
lista_sexo = []
maior_idade = 0
maior_nome = ""

mulheres = 0

for c in range(1, 5):
    nome = str(input("Qual o seu nome? "))
    idade = int(input("Qual a sua idade? "))
    sexo = str(input("Qual o seu sexo: (M/F) "))

    lista_idade.append(idade)
    if sexo == "M":
        if c == 1:
            maior_idade = idade
            maior_nome = nome
        else:
            if idade > maior_idade:
                maior_idade = idade
                maior_nome = nome
    if sexo == "F" and idade < 20:
        mulheres = mulheres + 1
media_idade = (lista_idade[0] + lista_idade[1] + lista_idade[2] + lista_idade[3]) / 4
print("A média de idade é: {} anos".format(media_idade))
print("O número de mulheres com menos de 20 anos é: {}".format(mulheres))
print("O homem mais velho se chama {} e tem {} anos.".format(maior_nome, maior_idade))
