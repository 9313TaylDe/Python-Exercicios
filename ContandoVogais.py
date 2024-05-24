palavra = input("Digite uma palavra: ")

vogais = sum(1 for char in palavra if char in 'aeiouAEIOU')

consoantes = sum(1 for char in palavra if char.isalpha() and char not in 'aeiouAEIOU')

print(f"Vogais: {vogais}, Consoantes: {consoantes}")