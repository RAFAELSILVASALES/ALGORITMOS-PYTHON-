
import random
n = int(input("\n digite qualquer numero para jogar | ou 0 para parar:"))
resultado = ''
escolha = ''
while n != 0:
    resultado = random.randint(1, 1000)
    escolha = str(
        input("\n digite se numero gerado  é Par ou | Ímpar:|ou digite N para sai do jogo|:"))
    respostar = escolha.lower()
    if respostar == 'n':
        break

    if (resultado % 2 == 0):
        result = 'par'

    if (resultado % 2 != 0):
        result = 'impar'

    if result == respostar:
        print('Acertou')
    else:
        print('Errou')
        print(f'numero certo era {resultado} e ele é {result}')
