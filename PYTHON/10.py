def contagem_caracter(s):
    resultado = {}

    for caracter in s:
        print(caracter)
        resultado[caracter] = resultado.get(caracter, 0) + 1
    return resultado


if __name__ == '__main__':
    print(contagem_caracter('banana'))
