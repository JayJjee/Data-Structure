num = int(input())
count = 0
for cont1 in range(num):
    ContazeroAux = 0
    fase = 0
    Contazero = input()

    for cont2 in Contazero:
        if cont2 == '1' and fase == 0:
            fase = 1

        elif cont2 == '0' and fase == 1:
            ContazeroAux += 1
            fase = 2

        elif cont2 == '0' and fase == 2:
            ContazeroAux += 1

        elif cont2 == '1' and fase == 2:
            count += ContazeroAux
            fase = 1
            ContazeroAux = 0
            
    print(count)
    count = 0