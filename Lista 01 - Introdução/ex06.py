def primos_gemeos(num):

    numPrimos = []
    firstPrimo = 3

    for i in range(1, num**2):
        secPrimo = firstPrimo + 2
        cont1 = 0
        cont2 = 0

        for j in range (1, secPrimo + 1):

            if firstPrimo % j == 0:
                cont1 += 1
            if secPrimo % j == 0:
                cont2 += 1

        if cont1 <= 2 and cont2 <= 2:
            numPrimos.append((firstPrimo, secPrimo))

            if len(numPrimos) == num:
                break

        firstPrimo = secPrimo
    return numPrimos

print(primos_gemeos(10))