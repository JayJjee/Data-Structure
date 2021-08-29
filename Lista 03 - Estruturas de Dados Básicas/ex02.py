class List:
    def __init__(self):
        self.lista = []

    def addRear(self, item):
        self.lista.insert(0,item)

    def addFront(self, item):
        self.lista.append(item)

    def removeRear(self):
        return self.lista.pop(0)

    def removeFront(self):
        return self.lista.pop()

    def isEmpty(self):
        return self.lista == []

lista = List()
listaFinal = List()
cctr = ''

while cctr != "X":
    entrada = input().split()
    cctr = entrada[0]

    if cctr == 'I':
        lista.addFront(entrada[1])
    elif cctr == 'F':
        lista.addRear(entrada[1])
    elif cctr == 'P':
        removido = lista.removeRear()
        listaFinal.addFront(removido)
    elif cctr == 'D':
        removido = lista.removeFront()
        listaFinal.addFront(removido)

while not listaFinal.isEmpty():
    print(listaFinal.removeRear())

while not lista.isEmpty():
    print(lista.removeFront())
