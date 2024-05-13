def maior():
    
    
    for i in range(1):
        numero1 = int(input("Digite: "))
        numero2 = int(input("Digite novamente: "))
        numero3 = int(input("Digite novamente: "))
        
        maior = numero1
        if numero2 > maior:
            print(f"O maior entre os números é {numero2}")
        if numero3 > maior:
            print(f"O maior entre os números é {numero3}")
        
      
            
maior()