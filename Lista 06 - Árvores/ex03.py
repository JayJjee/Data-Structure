def mostra_nivel_com_altura(raiz, n, altura):
    vertice = raiz
    if altura == n:
        mostra(vertice)
        print()
    if vertice.esq:
        mostra_nivel_com_altura(vertice.esq, n, altura+1)
    if vertice.dir:
        mostra_nivel_com_altura(vertice.dir, n, altura+1)

def mostra(raiz):

    print("(", end="")

    if raiz != None:

        print(raiz.dado, end="")
        print(" ", end="")
        mostra(raiz.esq)
        print(" ", end="")
        mostra(raiz.dir)
        
    print(")", end="")

def mostra_nivel(raiz, n):
    altura = 0
    mostra_nivel_com_altura(raiz, n, altura)