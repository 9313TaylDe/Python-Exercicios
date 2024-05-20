def matriculando():
    matematica1 = []
    contabilidade = []
    lista = 0

    while lista < 150:
        print("(1)Matematica --  (0)Sair")
        num = (int(input("Digite 1 para matematica: ")))
        if num == 0:
            break
        lista+=1
        matematica1.append(num)
    print("As matrículas na matematica1 são", matematica1)

    while lista < 100:
        print("(2)Direito  --  (0)Sair")
        num = int(input("Digite 2 para contabilidade: "))
        if num == 0:
            break
        lista += 1
        contabilidade.append(num)
    print("As matrículas na contabilidae são", contabilidade)
    
    conjunto_mat = set(matematica1)
    conjunto_con = set(contabilidade)
    
    resultado = conjunto_con.intersection(conjunto_mat)
    print("-----------------------------------------------------------")
    print("Os alunos matriculados tanto em contabilidade como em matematica são ", resultado)

matriculando()
