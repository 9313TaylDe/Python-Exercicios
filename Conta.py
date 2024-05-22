
def Saque(Saldo, Valor):
    if Saldo <= Valor:
        Saldo -= Valor
        print(f"Saque realizado com sucesso")
        return Saldo
    
    elif Valor > Saldo:
        return "Saldo insuficiente"
    
    Valor = 50
    Saldo_atual = 1000   
    novo_saldo = Saque(Saldo_atual, Valor)
    if isinstance(novo_saldo, str):
        print(novo_saldo)
    else:
        print("Saque realizado com sucesso")

          
def Extrato():
    print("-----EXTRATO-----")
    print(f"Nome: {Nome}")
    print(f"Saldo: R${Saldo}")
    print("CPF: 555-555-555.55")
    
    
def Depositar(Quantidade):
    Saque()
    Quantidade = 100
    deposito = Saldo + Quantidade
    Extrato()
    
Nome = input("Digite o nome: ")

    

while True:
        menu = input("[E] Extrato\n[X] Sair\n[S] Sacar\n[D] Depositar: ")
        if menu == 'x' or menu == 'X':
            print("Obrigado por utilizar!")
            
        if menu == 's' or menu == 'S':
            Saque()
            
        elif menu == 'e' or menu =='E':
            Extrato()
        elif menu =='d' or menu == 'D':
            Depositar()