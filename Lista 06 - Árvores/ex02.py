class ArvoreBinaria:
    def BinaryTree(raiz):
        return (raiz, (), ())

    def insertLeft(raiz):
        pass
''' def __init__(self, root):
        self.dado = root
        self.esq = None
        self.dir = None
    
    def insertEsq(self, newNode):
        if self.esq == None:
            self.esq = ArvoreBinaria(newNode)
        else:
            t = ArvoreBinaria(newNode)
            t.esq = self.esq
            self.esq = t
    
    def insertDir(self, newNode):
        if self.dir == None:
            self.dir = ArvoreBinaria(newNode)
        else:
            t = ArvoreBinaria(newNode)
            t.dir = self.dir
            self.dir = t'''

myTree = ArvoreBinaria()
print(myTree)
