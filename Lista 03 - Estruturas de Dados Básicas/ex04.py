import math
class Queue:
    def __init__(self):
        self.fila = []

    def dequeue(self):
        return self.fila.pop()

    def enqueue(self, item):
        self.fila.insert(0,item)

    def isEmpty(self):
        return self.fila == []

    def size(self):
        return len(self.fila)

fila = Queue()
tarPriori = input().split()
atvRealizada = int(input())
atvRestam = math.ceil(len(tarPriori)/2) - atvRealizada

print(f"Tamanho da fila: {atvRestam}")

