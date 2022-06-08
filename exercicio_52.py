# verificar se o numero é primo
from time import sleep

numero = int(input("Digite um número: "))

tot = 0
for c in range(1, numero+1, 1):
   if numero % c == 0:
       print("\033[31m", end=" ")
       tot = tot + 1
   else:
       print("\033[32m", end=" ")
   print("{}".format(c), end=" ")

print("\nO número {} foi divisível {} vezes.".format(numero, tot))
sleep(2)
if tot == 2:
    print("\033[32mO número {} é primo.\033[m".format(numero))
else:
    print("\033[1:33mO número {} não é primo.\033[m".format(numero))

