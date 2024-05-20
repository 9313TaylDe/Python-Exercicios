equipe_1 = []
equipe_2 = []
equipe_3 = []
equipe_4 = []

lista = 0

while lista < 10:
        print("( ")
        nome = (input("Digite S para sair ou digite um nome: "))
        if nome == 's':
            break
        lista+=1
        equipe_1.append(nome)
        print("As matrículas na equipe1 são", equipe_1) 
while lista < 10:
        print("( ")
        nome = (input("Digite S para sair ou digite um nome: "))
        if nome == 's':
            break
        lista+=1
        equipe_2.append(nome)
        print("As matrículas na equipe2 são", equipe_2) 
while lista < 10:
        print("( ")
        nome = (input("Digite S para sair ou digite um nome: "))
        if nome == 's':
            break
        lista+=1
        equipe_3.append(nome)
        print("As matrículas na equipe3 são", equipe_3) 
while lista < 10:
        print("( ")
        nome = (input("Digite S para sair ou digite um nome: "))
        if nome == 's':
            break
        lista+=1
        equipe_4.append(nome)
        print("As matrículas na equipe4 são", equipe_4) 
        
        
equipe_11 = set(equipe_1)
equipe_22 = set(equipe_2)
equipe_33 = set(equipe_3)
equipe_44 = set(equipe_4)
        
resultado = equipe_11.intersection(equipe_22)
resultado2 = equipe_33.intersection(equipe_44)
resultado_final = resultado.intersection(resultado2)
        
print(resultado_final)

    
        
#MOSTRE OS NOMES DOS INTEGRANTES DAS EQUIPES
#MOSTRE A INTERSECÇÃO DAS EQUIPES