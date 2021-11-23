#!/usr/bin/python3

banco_1 = [
	["pedro" , 0], 
	["juan"  , 0],
	["marcos", 0],
	["diego" , 0],
	["ana"   , 0]
]
print (banco_1)
import random
# print(random.randrange(0, 999999))

for cuenta in banco_1:
	cuenta[1] = random.randrange(0, 999999)

print (banco_1)

banco_2 = [
	["alex" , 1000], 
	["juan"  , 3000],
	["marta", 5000],
	["ana" , 1000]
]
print (banco_2)

# ------------------------------------------------------
def titulares(banco):
	respuesta = []
	for cuenta in banco:
		respuesta.append(cuenta[0])
	return respuesta

print(titulares(banco_1))
print(titulares(banco_2))

# ------------------------------------------------------
def titular(cuenta): return(cuenta[0])

def posicion(banco,titular):
	return titulares(banco).index(titular)

def ingreso(banco,titular,importe):
	if not titular in titulares(banco):
		print ("ingreso no efecutado")
		return
	#assert: titular in titulares
	banco[posicion(banco,titular)][1] += importe

banco_3 = []
for cuenta in banco_1:
	banco_3.append(cuenta)
	if titular(cuenta) in titulares(banco_2):
		# print (titular(cuenta))
		# print (posicion(banco_2, titular(cuenta)))
		# print (banco_2[posicion(banco_2, titular(cuenta))])
		# print (banco_2[posicion(banco_2, titular(cuenta))][1])		
		ingreso(banco_3, titular(cuenta), banco_2[posicion(banco_2, titular(cuenta))][1])

print (banco_3)

