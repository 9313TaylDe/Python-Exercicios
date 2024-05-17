frutas = ("laranja","maca","uva")

letras = tuple("python")

numeros = tuple([1,2,3,4,5,])

pais = ("Brasil")

frutas[0]
frutas[2]
frutas[-1]
frutas[-2]

print(frutas[2])


tuple = ("p","y","t","h","o","n")

print(tuple[2:])
print(tuple[:2])
print(tuple[1:3])
print(tuple[0:3:2])
print(tuple[::])
print(tuple[::-1])

#----------------------------------------------------------------------------

carros = ("gol","palio","chevrolet")
for carro in carros:
    print(carro)
    
    
carros =("gol","palio")
for indice, carro in enumerate(carros):
    print({indice}, {carros})
    
    
    
#-----------------------------------------------------------------------------


numeros = {1,2,3,4,5,6,}

numeros = ["frutas"]#listas

frutas = ("larajna", "maca")#tupla

numeros = list(numeros)

numeros = [0]

#----------------------------------------------------------------------------

pessoa = {"nome": "Gustavo", "idade": 28}

#-----------------------------------------------------------------------------


carros4 = {"marca": "gol", "ano": 1945}
print(carros4)
carros2 = ("marca", "gol", "ano")
print(carros2)
carros3 = ["marca", "gol", "ano"]
print(carros3)

carros3[0] = "model"



#----------------------------------------------------------------------------

carros = {"Marca": "Gol", "Fabricante": "Wolksvagen", "Valor":5000}
carros.get['dono','Não tem dono']