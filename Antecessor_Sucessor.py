def funcao():
    for i in range(0,1):
        numero = int(input("Digite um número: "))

    sucessor = numero + 1
    antecessor = numero - 1

    return print(f"O antecessor do número {numero} é {antecessor} e o sucessor é {sucessor}")

funcao()