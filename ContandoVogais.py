def ContaVogais():
    
    palavra = input("Digite uma palavra: ")
    vogais = 'aeiouAEIOU'
    consoantes = not 'aeiouAEIOU'
    somandoVogais = 0
    for letra in palavra:
        if letra in vogais:
            somandoVogais += 1
            print("Achei a quantidade de "+letra)
ContaVogais()