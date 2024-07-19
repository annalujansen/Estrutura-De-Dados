class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        return None

    def peek(self):
        if len(self.items) > 0:
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

pilha = Stack()  

anilhaDesejada = None

while True:
    n = int(input())
    
    if n == 0:
        anilhaDesejada = int(input())
        break
    pilha.push(n)    
    
lista = []
soma = 0
while not pilha.isEmpty():
    item = pilha.pop()
    lista.append(item)
    soma += item
    if item == anilhaDesejada:
        break
for i in lista:
    if i != 0:
        print(f'Peso retirado: {i}')
print(f'Anilhas retiradas: {len(lista)}')
print(f'Peso total movimentado: {soma}')