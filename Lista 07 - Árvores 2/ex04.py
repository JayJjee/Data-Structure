def constituiArvoreBinariaDeBusca(raiz):
    bTree = True
    if raiz.esq != None:
        bTree = constituiArvoreBinariaDeBusca(raiz.esq)
    if raiz.dir != None:
        bTree = constituiArvoreBinariaDeBusca(raiz.dir)
    if raiz.esq != None and raiz.esq.dado > raiz.dado:
        return False
    if raiz.dir != None and raiz.dir.dado < raiz.dado:
        return False
    return bTree
