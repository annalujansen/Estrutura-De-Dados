import math
'''
numb = float(input())
numero = numb/2
seno = math.sin(numero)
resul = seno**2

print(resul)
'''

L1=float(input("L1: "))
L2=0.948
M1=0.35446
M2=0.34716

momentoDeInercia = M1*(L1)**(1/2) + M2*(L2)**(1/2)
torque = M1*L1 + M2*L2

divisao = momentoDeInercia/torque

dentroRaiz = ((1/9.8)*divisao)**(1/2)

periodo = 2*math.pi*dentroRaiz

print(momentoDeInercia)
print(torque)
print(divisao)
print(dentroRaiz)
print(periodo)
