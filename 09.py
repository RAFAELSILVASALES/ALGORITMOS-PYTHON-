# Escreva  um  programa  que  leia  o  valor  dos  dois  catetos  de  um  triângulo  retângulo  e calcule o valor da hipotenusa.
import math
catetoA = int(input("\n digite valor do primeiro cateto:"))
catetoB = int(input("\n digite valor do segundo cateto:"))

hipotenusa = (catetoA ** 2) + (catetoB ** 2)
raiz = math.sqrt(hipotenusa)
arendondamento = round(raiz, 2)
print(f'O valor da hipotenusa é {arendondamento}')
