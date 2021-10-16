def mostra(raiz):

    print("(", end="")

    if raiz != None:

        print(raiz.dado, end="")
        print(" ", end="")
        mostra(raiz.esq)
        print(" ", end="")
        mostra(raiz.dir)
        
    print(")", end="")