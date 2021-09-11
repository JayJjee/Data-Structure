def fibonacci(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    listFibo = [0,1]
    for cont in range(n-1):
        aux = listFibo[cont] + listFibo[cont+1]
        listFibo.append(aux)
    listFibo.pop()
    return listFibo