a = []
titular = 0
reserva = 0
total = 0
qntReserva = 0

jogadores =  int(input())
habilidade = list(input().split())

if len(habilidade) == jogadores:
    for cont1 in range(len(habilidade)):
        a.append(int(habilidade[cont1]))
        a.sort(reverse=True)

    for cont2 in range(11):
        titular += a[cont2]

    for cont3 in range(11, len(habilidade)):
        qntReserva += 1
        if qntReserva <= 11:
            reserva += a[cont3]

diferenca = titular - reserva
print(diferenca)