import math

def cal_hipotenusa():
    
    catetoA =float(input("Digite o cateto adjacente: "))
    catetoO =float(input("Digite o cateto oposto: "))
    hipotenusa =  math.sqrt(catetoA**2 + catetoO**2)
    
    
    return print(f"A hipotenusa é {hipotenusa:.2f}")

cal_hipotenusa()