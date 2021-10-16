class Tree:
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None

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

def inserirABB(raiz, no):
    if raiz is None:
        raiz = no
    elif no.valor > raiz.valor:
        if raiz.right is None:
            raiz.right = no
        else:
            inserirABB(raiz.right, no)
    else: 
        if raiz.left is None:
            raiz.left = no
        else:
            inserirABB(raiz.left, no)

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
        inserirABB(raiz, Tree(entradaNum))
    if entrada == 'in':
        raiz.printEmOrdem()
        print()
    if entrada == 'pre':
        raiz.printPreOrdem()
        print()
    if entrada == 'pos':
        raiz.printPosOrdem()
        print()
