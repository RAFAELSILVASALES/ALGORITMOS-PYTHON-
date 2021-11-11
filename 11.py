
import random

n = int(input("\n digite qualquer numero para jogar | ou 0 para parar:"))
resultado = ''
while n != 0:
    resultado = random.randint(1, 6)
    print(f'\n o resultado gerado é {resultado}')
    n = int(input("\n digite qualquer numero para jogar | ou 0 para parar:"))
