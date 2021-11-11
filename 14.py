

palavra = 'banana'
respostar = ''
continua = str(
    input("\n digite qualquer numero para continuar ou | 0 para sair:"))
while continua != '0':
    respostar = str(input("\n tente adivinha uma palavra: "))

    if respostar == palavra:
        print(f"parabêns, você acertou a palavra é {palavra}")
        break

    if respostar != palavra:
        print(" você errou a dica é  uma fruta")
        respostar = str(input("\n tente adivinha a palavra: "))

    if respostar != palavra:
        print(" você errou a dica é uma  palvara que  tem três vogais iguais")
        respostar = str(input("\n tente adivinha a palavra: "))
    if respostar != palavra:
        print(" você errou a dica é uma  palvara que tem três vogais iguais a vogal é A")
