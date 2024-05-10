def soma():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))

    soma = n1 + n2
    print(f"A soma de {n1} + {n2} = {soma}")
    return soma
def multiplicaca():
    n1 = int(input("Digite um número e veja a sua multiplicação: "))
    for i in range(1,10):
        multiplica = n1 * i
        print(f"{n1} x {i} = {multiplica}")
    
    
multiplicaca()