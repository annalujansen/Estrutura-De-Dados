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
    
def calcular_tempo_total(N, F, P, pesos):
    fila = Queue()
    for peso in pesos:
        fila.put(peso)  # Adiciona os pesos dos veículos na fila
    
    tempo_total = 0
    
    while not fila.empty():
        for i in range(F):
            if fila.empty():
                break
            
            peso = fila.get()  # Remove o veículo da frente da fila
            
            if i == 0:  # Apenas fiscaliza veículos conforme o fator de amostragem
                if peso > P:
                    tempo_total += 10  # Veículo é fiscalizado e está acima do peso
                    fila.put(peso - 2)  # Veículo descarta 2kg e vai para o final da fila
                else:
                    tempo_total += 5  # Veículo é fiscalizado e está dentro do limite
            else:
                tempo_total += 1  # Veículo é liberado diretamente

    return tempo_total

# Leitura da entrada
N, F, P = map(int, input().split())
pesos = list(map(int, input().split()))

# Cálculo do tempo total
tempo_total = calcular_tempo_total(N, F, P, pesos)

# Impressão do resultado
print(tempo_total)
