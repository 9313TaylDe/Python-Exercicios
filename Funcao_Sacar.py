def sacar(saque = int(input("Digite um valor: "))):
    saldo = 10
    status = "Sucesso" if saldo >= saque else "Falha"
    print(f"{status} operação")
    
    numbers = [1,2,3,4,5]
    for num in numbers:
        if num == 3:
            break
        print(num)
    
sacar()