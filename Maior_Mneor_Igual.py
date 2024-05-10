def descubra():
    i = 0
    numero = 0
    numero =  int(input("Digite um número: "))
    numero2 = int(input("Digite o segundo número: "))

    if(numero > numero2):
            print(f"Números {numero} maior que o {numero2}")
    elif(numero < numero2):
            print(f"Número {numero} menor que o {numero2}")
    else:
           print(f"Os números {numero} e {numero2} são iguais")


descubra()