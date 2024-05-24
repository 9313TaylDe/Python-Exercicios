def ContaVogais():
    
    palavra = input("Digite uma palavra: ")
    
    vogais = 'aeiouAEIOU'
    numbers = 1,2,3,4,5,6,7,8,9
    consoantes = not 'aeiouAEIOU'
    somandoVogais = 0
    espaco = 0
    
    for letra in palavra:
        if letra in vogais:
            somandoVogais += 1
            print("Achei a quantidade de "+letra)
        
        elif letra == ' ':
            espaco += 1
            
        else:
                consoantes += 1
            
ContaVogais()