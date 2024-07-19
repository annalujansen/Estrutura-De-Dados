class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.insert(0, item)  

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Dequeue from an empty queue")
        return self.items.pop()  

    def size(self):
        return len(self.items)
   
class EternalQueue:
    def __init__(self):
        self.queue = Queue()  

    def advance(self, n):
        for _ in range(n):
            self.queue.enqueue(self.queue.dequeue())

    def get_front_and_end(self):
        frente = self.queue.items[-1] if not self.queue.isEmpty() else None
        fim = self.queue.items[0] if not self.queue.isEmpty() else None
        return frente, fim


fila_eterna = EternalQueue()
nomes = input().split()

for nome in nomes:
    fila_eterna.queue.enqueue(nome)

n=int(input())
fila_eterna.advance(n)

pessoa_frente, pessoa_fim = fila_eterna.get_front_and_end()

print(f"Pessoa da frente: {pessoa_frente}")
print(f"Pessoa do fim: {pessoa_fim}")
