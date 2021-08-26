import re

dataInicial = []
dataFinal = []

data1 = re.split(r'\s+|:', input())
data2 = re.split(r'\s+|:', input())

for cont in range(4):
    dataInicial.append(int(data1[cont]))
    dataFinal.append(int(data2[cont]))

if dataInicial[0] > dataFinal[0]:
    print('Data inválida!')
elif dataInicial[1] > 23 or dataFinal[1] > 23:
    print('Data inválida!')
elif dataInicial[2] > 59 or dataFinal[2] > 59:
    print('Data inválida!')
elif dataInicial[3] > 59 or dataFinal[3] > 59:
    print('Data inválida!')
else:
    finalDay = dataFinal[3] + (dataFinal[2]*60) + (dataFinal[1]*3600) + (dataFinal[0]*86400)
    firstDay = dataInicial[3] + (dataInicial[2]*60) + (dataInicial[1]*3600) + (dataInicial[0]*86400)

    resultado = finalDay - firstDay
    duracaoDia = resultado // 86400
    duracaoDiaSeg = duracaoDia * 86400
    duracaoHora = (resultado - duracaoDiaSeg) // 3600
    duracaoHoraSeg = duracaoHora * 3600
    duracaoMinuto = (resultado - duracaoDiaSeg - duracaoHoraSeg) // 60
    duracaoMinutoSeg = duracaoMinuto * 60
    duracaoSegundo = resultado - duracaoDiaSeg - duracaoHoraSeg - duracaoMinutoSeg

    print(f'{duracaoDia} dia(s)')
    print(f'{duracaoHora} hora(s)')
    print(f'{duracaoMinuto} minuto(s)')
    print(f'{duracaoSegundo} segundo(s)')