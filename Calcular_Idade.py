nome = input("Digite o seu bnome: ")
idade = int(input("Digite a sua idade: "))

if idade <= 17 or idade > 60:
    print(f'{nome} você não é obrigado ou não pode votar!')

elif idade >= 18 and idade < 60:
    print(f"{nome}, o seu voto obrigaório!")
    print("-------------------------------")