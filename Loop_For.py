texto = input("Informe um texto: ")

vogais = "AEIOU"

for letra in texto:
    if letra.upper() in vogais:
        print(letra, end='...')


i = 2
for i in range(10):
    a = 2
    multiplica = a * i
    print(f"{a} * {i} = {multiplica}")