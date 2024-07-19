class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
class Pessoa:
    def __init__(self,nome,idade,especial):
        self.nome = nome
        self.idade = idade 
        self.especial = especial
    
    def __repr__(self):
        return f'{self.nome}, Idade: {int(self.idade)}, É especial: {self.especial}'

class filaPrioridade:
    def __init__(self):
        self.f1 = Queue()
        self.f2 = Queue()
        self.f3 = Queue()


anna = Pessoa('Anna',25,False)
print(anna)