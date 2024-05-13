def soma():
    for i in range(0,2):
       numero = int(input(f"Digite um numero: "))
       
       soma = numero + numero
       produto = numero * numero
       media = soma / 2
    
    return print(f"A soma é {soma}\nO produto é {produto}\nA média é {media}")

soma()