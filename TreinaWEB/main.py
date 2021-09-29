from Vetores import vetor

print(30 * '-', "MENU", 30 * '-')
print("1. Vetores")
print("2. Listas Ligadas")


menu = int(input("Digite a opção desejada: "))

if menu == 1:
    vetorTeste = vetor.Vetor(0)
    vetorTeste.inserir_elemento_posicao(1, 0)
    vetorTeste.inserir_elemento_posicao(2, 1)
    vetorTeste.inserir_elemento_posicao(3, 2)
    vetorTeste.inserir_elemento_posicao(4, 2)
    vetorTeste.inserir_elemento_posicao(5, 2)
    '''vetorTeste.inserir_elemento_final(1)
    vetorTeste.inserir_elemento_final(2)
    vetorTeste.inserir_elemento_final(3)
    vetorTeste.inserir_elemento_final(4)'''
    '''print(vetorTeste.listar_elemento(0))
    print(vetorTeste.listar_elemento(1))
    print(vetorTeste.listar_elemento(2))
    print(vetorTeste.listar_elemento(3))'''
    print(vetorTeste)
    print(vetorTeste.contem(3))
    print(vetorTeste)
    print(vetorTeste.indice(5))