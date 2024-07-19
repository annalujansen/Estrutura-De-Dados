class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return f"Pilha: {self.items}"
    
class Fila_comPilhas:
    def __init__(self):
        self.pilha1 = Stack()
        self.pilha2 = Stack()

    def enqueue(self, item):
        return self.pilha1.push(item)
        #print(f"Pilha 1 após enqueue: {self.pilha1}")

    def dequeue(self):
        if self.pilha1.isEmpty() and self.pilha2.isEmpty():
            return None

        if self.pilha2.isEmpty():
            while not self.pilha1.isEmpty():
                self.pilha2.push(self.pilha1.pop())
            #print(f"Pilha 2 após mover elementos da Pilha 1: {self.pilha2}")

        #print(f"Pilha 2 após dequeue: {self.pilha2}")
        return self.pilha2.pop()

    def imprime(self):
        if self.pilha2.isEmpty():
            while not self.pilha1.isEmpty():
                self.pilha2.push(self.pilha1.pop())
            #print(f"Pilha 2 após mover elementos da Pilha 1: {self.pilha2}")

        while not self.pilha2.isEmpty():
            print(f'{self.pilha2.peek()}')
            self.pilha2.pop()

        while not self.pilha1.isEmpty():
            self.pilha2.push(self.pilha1.pop())
        #print(f"Pilha 2 após mover elementos da Pilha 1 pela 2ª vez: {self.pilha2}")

        while not self.pilha2.isEmpty():
            print(f'{self.pilha2.peek()}')
            self.pilha2.pop()

	
fila = Fila_comPilhas()

fila.enqueue(1)
fila.enqueue(2)
fila.enqueue(3)
fila.enqueue(4)
fila.enqueue(5)
print('dequeue - '+str(fila.dequeue()))
fila.enqueue(6)
print('dequeue - '+str(fila.dequeue()))
print('dequeue - '+str(fila.dequeue()))
fila.enqueue(7)
fila.enqueue(8)
fila.imprime()