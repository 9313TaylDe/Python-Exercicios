def positivos():
    num = 1
    soma = 0
    
    while num >= 0:
        soma = 0
        num = int(input("Informe o número (0) para sair: "))
        if num > 1:
            
            for i in range(0, num):
                if i % 2 == 0:
                    continue
                else:
                    print(i)
                    soma += i
                print(f" + "+" = {soma}")
            
        elif  num == 0:
            break      
        else:
            print("Número inválido. Digite novamente")
    
    
           
positivos()    