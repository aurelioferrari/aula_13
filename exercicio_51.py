#ler o primeiro termo e a razao de uma PA e mostrar os 10 primeiros termos

pa = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
print("O primeiro termo é: {}".format(pa[0]))
razao = pa[1] / pa[0]
print("A razão da PA é: {}".format(razao))

for c in range(0, 10):
    print(pa[c])