def contagem_caracter(s):
    caracteres_ordenados = sorted(s)

    caracteres_anterior = caracteres_ordenados[0]
    contagem = 1

    for caracter in caracteres_ordenados[1:]:
        if caracter == caracteres_anterior:
            contagem += 1

        else:
            print(f'{caracteres_anterior}: {contagem}')
            caracteres_anterior = caracter
            contagem = 1
    print('f{caracteres_anterior}: {contagem}')


if __name__ == '__main__':
    contagem_caracter('banana')
