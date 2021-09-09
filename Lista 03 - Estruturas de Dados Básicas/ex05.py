class List:
    def __init__(self):
        self.lista = []

    def addRear(self, item):
        self.lista.append(item)

    def addFront(self, item):
        self.lista.insert(0,item)

    def removeRear(self):
        return self.lista.pop()
        

    def removeFront(self):
        return self.lista.pop(0)

    def isEmpty(self):
        return self.lista == []

entrLista = List()
cctr = ''
praRemover = []

while cctr != "X":
    entrada = input().split()
    cctr = entrada[0]
    
    if cctr == 'I':
        entrLista.addFront(entrada[1])
    elif cctr == 'F':
        entrLista.addRear(entrada[1])
    elif cctr == 'P':
        removido = entrLista.removeRear()
        print(removido)
    elif cctr == 'D':
        removido = entrLista.removeFront()
        print(removido)
    elif cctr == 'V':
        removidoemV = entrada[1]
        cont2 = 0
        for cont in range(len(entrLista.lista)):
            if entrLista.lista[cont] == removidoemV:
                entrLista.lista.pop(cont)
                cont2+=1
        print(cont2)
    elif cctr == 'E':
        posiemV = int(entrada[1])
        removidoemV = entrLista.lista.pop(posiemV-1)
        print(removidoemV)
    elif cctr == 'T':
        removidoemV = entrada[1]
        addemV = entrada[2]
        for cont in range(len(entrLista.lista)):
            if entrLista.lista[cont] == removidoemV:
                entrLista.lista[cont] = addemV
                break
    elif cctr == 'C':
        cont2 = 0
        numentr = entrada[1]
        for cont in range(len(entrLista.lista)):
            if entrLista.lista[cont] == numentr:
                cont2 += 1
        print(cont2)

    print()
    print(entrLista.lista)
    print()

print()

while not entrLista.isEmpty():
    print(entrLista.removeFront())

"""	
I 45
F 32
I 45
F 12
F 45
T 32 12
E 5
V 12
P
D
X
"""