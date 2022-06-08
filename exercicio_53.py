# verificar se a frase é um palindromo

# juntando as palavras e tirando os espaços
frase = str(input("Digite uma frase: ")).strip().upper()
frase = frase.split()
junto = "".join(frase)

# criando a string inversa
inverso = ""

# pegando cada letra da frase junto de modo invertido e adicionando em inverso

for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]

# comparando strings
if junto == inverso:
    print("Isso é um palíndromo.")
else:
    print("Isso não é um palíndromo.")

# outra maneira de inverter uma string é inverso = junto[::-1]