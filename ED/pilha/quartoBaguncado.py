class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)


def organiza(roupa):
    ...    


tipo=Stack()
cor=Stack()
sum = 0
n=int(input())    
for _ in range(n):
    entrada = input()
    parts=entrada.split()
    
    type=parts[0]
    color=parts[1]
    time=parts[2]

    tipo.push(type)
    cor.push(color)
    time=int(time)
    sum+=time

while not tipo.isEmpty() and not cor.isEmpty():
    print(f'Tipo: {tipo.pop()}, Cor: {cor.pop()}')
print(f'Total de roupas: {n}')
print(f'Total de tempo: {sum}')