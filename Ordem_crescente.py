def ordenando():
    vetor = []
    auxiliar = 0
    
    for i in range(5):
        numero = int(input("Digite um número: "))
        vetor.append(numero)
        
        vetor.sort()
        
    for numero in vetor:
        print("\nOrdenando: ",numero, end=" ")
       
        
        
ordenando()
        