def desconto():
        preco = float(input("Digite o preço: "))
        nome = input("Digite o seu nome: ")
        sexo = input("Digite o seu sexo: ")
        
        
        if sexo.lower() == "f":
            print("No dia das mulheres, toda mulher recebe 30% de desconto em todos os nossos produtos femininos.")
            print(f"Nome: {nome}\nSexo: {sexo}")
            desconto = (preco * 0.3)
            print(f"O valor com desconto é: ", preco - desconto)
            
        elif sexo.lower() == "m":
            print(f"Nome: {nome}\nSexo: {sexo}")
            desconto = (preco *0.05)
            print("O valor com desconto é: ", preco - desconto)
            
desconto()
        
    
    