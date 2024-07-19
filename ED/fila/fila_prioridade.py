class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Pessoa:
    def __init__(self, especial, idade, nome):
        self.especial = especial
        self.idade = idade
        self.nome = nome

    def __repr__(self):
        return f'{self.nome} com priopridade({self.especial}) e idade {self.idade}'

class FilaPrioridade:
    def __init__(self):
        self.geral = [Queue(), Queue(), Queue()]

    def enqueue(self, pessoa):
        if pessoa.idade >= 80:
           self.geral[0].enqueue(pessoa)
        elif pessoa.idade >= 60 or pessoa.especial:
           self.geral[1].enqueue(pessoa)
        else:
           self.geral[2].enqueue(pessoa)

    def dequeue(self):  
        for q in self.geral:
           if q.size():
              return q.dequeue()

    def size(self):
        c = 0
        for q in self.geral:
            c+= q.size()
        return c
   
   
   
prio = FilaPrioridade()

for i in range(5):
    aux = input().split()
    pes = Pessoa(int(aux[2]), int(aux[1]), aux[0])
    prio.enqueue(pes)

while(prio.size() > 0):
   print(prio.dequeue())














































































