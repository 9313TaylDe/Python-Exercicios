#1. Criar listas de:
#  1.1. matematica1
# 1.2. contabilidade1

matematica1 = []
contabilidade1 = []
'''
3. Cadastrar os alunos por disciplina
  3.1 Criar uma repetição até no máximo de 150 para a lista de matemática1
'''
lista = 0
while lista<150:
  matematica1[lista]= input('Entre com o num. da matr. para Matemática1, ou 0 pra sair: ')
  if matematica1[lista] == 0: break
  lista = lista + 1
  
# 4. Comparar as matrículas que estão nas duas listas
# Exemplo:
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.intersection(conjunto_b)
print(resultado)