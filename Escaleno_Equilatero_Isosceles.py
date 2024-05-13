def escaleno():
    A = float(input("Digite o valor da reta A: "))
    B = float(input("Digite o valor da reta B: "))
    C = float(input("Digite o valor da reta C: "))
    
    if A == B and A == C and B == C:
        print(f"Com as seguintes medidas, teremos umm triângulo equilátero: {A} {B} {C}")
    elif A == B  or B == C or A == C:
        print(f"Com as seguintes medidas, teremos umm triângulo isósceles: {A} {B} {C}")
    if A != B and A != C and B != C:
        print(f"Com as seguintes medidas, teremos umm triângulo escaleno: {A} {B} {C}")
        
escaleno()