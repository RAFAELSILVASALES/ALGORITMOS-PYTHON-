print("""                 menu
você conhecia a vítima digite 1 para sim ou 2 para não:
você esteve com a vítima no dia do assassinato 1 para sim ou 2 para não:
você devia dinheiro para vítima 1 para  sim ou 2 para não:
 """)

pergunta1 = int(input("\n você conhecia a vítima? :"))
pergunta2 = int(
    input("\n você esteve com a vítima no dia do assassinato? :"))
pergunta3 = int(input("\n você devia dinheiro para vitima ? :"))

if pergunta1 == 1 and pergunta2 == 1 and pergunta3 == 1:
    print("culpado")
else:
    if (pergunta1 == 1 and pergunta3 == 1):
        print("suspeito")


if pergunta1 == 2 and pergunta2 == 2 and pergunta3 == 2:
    print("inocente")
