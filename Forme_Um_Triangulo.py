def FormarTriangulo():
    
    A = float(input("Digite o valor da reta A: "))
    B = float(input("Digite o valor da reta B: "))
    C = float(input("Digite o valor da reta C: "))
    
    if A + B > C and B + C > A and C + A> B:
        print("Digite números maiores que 0\n")
        return print(f"Você pode formar um seguintes com as seguintes medidas:  {A} {B} {C} ")
    else:
        return print("Valores inválidos: ")

FormarTriangulo()