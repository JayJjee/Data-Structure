class Tree:
    def __init__(self, valor = None):
        if valor != None:
            self.valor = valor
        else:
            self.valor = None
        self.left = None
        self.right = None

    def insert(self, valor):
        if self.valor:
            if valor < self.valor:
                if self.left is None:
                    self.left = Tree(valor)
                else:
                    self.left.insert(valor)
            elif valor > self.valor:
                    if self.right is None:
                        self.right = Tree(valor)
                    else:
                        self.right.insert(valor)
        else:
            self.valor = valor

    def printEmOrdem(self):
        if self.left:
            self.left.printEmOrdem()
        print(self.valor, end=' ')
        if self.right:
            self.right.printEmOrdem()
    
    def printPreOrdem(self):
        print(self.valor, end=' ')
        if self.left:
            self.left.printPreOrdem()
        if self.right:
            self.right.printPreOrdem()

    def printPosOrdem(self):
        if self.left:
            self.left.printPosOrdem()
        if self.right:
            self.right.printPosOrdem()
        print(self.valor, end=' ')

entrada = input()

while entrada.isnumeric() == False:
    print()
    entrada = input()

if entrada.isnumeric() == True:
    entradaNum = int(entrada)
    raiz = Tree(entradaNum)

while entrada != 'quack':
    entrada = input()
    if entrada.isnumeric():
        entradaNum = int(entrada)
        raiz.insert(entradaNum)
    if entrada == 'in':
        raiz.printEmOrdem()
        print()
    if entrada == 'pre':
        raiz.printPreOrdem()
        print()
    if entrada == 'pos':
        raiz.printPosOrdem()
        print()
