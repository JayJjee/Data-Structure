def nivel_com_altura(raiz, no, altura):
    alturaLeft = -1
    alturaRight = -1
    if no == raiz.dado:
        return altura
    if raiz.esq:
        alturaLeft = nivel_com_altura(raiz.esq, no, altura + 1)
    if raiz.dir:
        alturaRight = nivel_com_altura(raiz.dir, no, altura + 1)
    if alturaLeft != -1:
        return alturaLeft
    if alturaRight != -1:
        return alturaRight
    return -1

def nivel(raiz, no):
    altura = 0
    return nivel_com_altura(raiz, no, altura)