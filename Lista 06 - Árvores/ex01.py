def altura(raiz):

    no = raiz
    alturaRight = -1
    alturaLeft = -1
    if raiz == None or raiz == 0:
        return 0
    if no.esq:
        alturaLeft = -1
        alturaLeft = altura(no.esq)
    if no.dir:
        alturaRight = -1
        alturaRight = altura(no.dir)

    if alturaRight > alturaLeft:
        return alturaRight + 1
    return alturaLeft + 1
