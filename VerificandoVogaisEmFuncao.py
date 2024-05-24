def verificar(string):
    vogais = 'aeiouAEIOU'
    for letra in palavra:
        vogais = 'aeiouAEIOU'
        num_vogais = sum(1 for char in string if char in vogais)
        num_consoantes = sum(1 for char in string if char.isalpha() and char not in vogais)
        return num_vogais, num_consoantes
palavra = input("Digigte a palavra")
vogais, consoantes = verificar(palavra)
print(f"Vogais: {vogais}\nConsoantes: {consoantes}")
