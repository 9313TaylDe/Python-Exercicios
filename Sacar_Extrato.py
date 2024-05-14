def sacar():
    saldo = float(input("Digite o valor do saldo: "))

    opcao1 = 10


    cheque_especial = 10
    while opcao1 != 0:
        opcao1 = int(input("Escolha \nConta normal = 1: \nConta Universitaria = 2: \nSair - 0")) 
        conta_normal = True if opcao1 == 1 else False
        if conta_normal:
                opcao2 = int(input("Escolha \n1 - Saque:\n2 - Extrato:  "))
                if opcao2 == 1:
                    saque = float(input("Digite o valor do saque: "))
                    if saldo >= saque: 
                        print("Operação bem sucedida!")
                    elif saldo + cheque_especial >= saque:
                        print("Saque realizado mediante o cheque especial")
                    else:print("Saldo insuficiente")
                if opcao2 == 2:
                    print("Exibindo extrato")
        elif opcao1 == 2:
                opcao2 = int(input("Escolha \n1 - Saque:\n2 - Extrato:  "))
                if opcao1 == 1:
                    saque = float(input("Digite o valor do saque: "))
                    if saldo >= saque:
                        print("Operação bem sucedida!")
                        break
                    elif saldo  >= saque:
                        print("Saldo insuficiente")
                        break
                elif opcao2 == 2:
                    print("Exibindo o extrato")
        else:
            print("Opção inválida")
    print("Saíndo!")
    
sacar()