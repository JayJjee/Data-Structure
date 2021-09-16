notFibo = []

def fibonacci(n):
    finalRange = 0
    while len(notFibo) < n:
        finalRange += 1
        listFibo = [0,1]
        for cont in range(finalRange):
            aux = listFibo[cont] + listFibo[cont+1]
            listFibo.append(aux)
        for cont2 in range(listFibo[-2], listFibo[-1]):
            if cont2 > listFibo[-2] and cont2 < listFibo[-1]:
                notFibo.append(cont2)
    print(listFibo)
    print(notFibo)

num = int(input())
fibonacci(num)
if num == 1:
    print(notFibo[0])
else:
    for cont3 in range(num-1):
        print(notFibo[cont3], end=', ')
    print(notFibo[cont3+1])