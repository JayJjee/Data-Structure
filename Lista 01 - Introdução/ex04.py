import math

cont = 0
i = 1
j = 0
incByte = 0

dados = int(input())
print(f'Transmitindo {dados} bytes...')
while cont < dados:
    byte = int(input())
    cont += byte
    incByte += byte
    if i == 5:
        if incByte == 0:
            print(f'Tempo restante: pendente...')
            i = 0
        else:  
            temporesta = (float(f'{(dados - cont) / (incByte / 5):.6f}'))
            if cont < dados:
                print(f'Tempo restante: {math.ceil(temporesta)} segundos.')
            i = 0
        incByte = 0
    j += 1
    i += 1
    if cont >= dados:
        print(f'Tempo total: {j} segundos.')