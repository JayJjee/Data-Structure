def mdc(num1, num2):
    if num2 == 0:
        return num1

    resto = num1 % num2
    num1 = num2
    num2 = resto

    return mdc(num1, num2)

num1 = 0
num2 = 0
numeros = input().split()
num1 = int(numeros[0])
num2 = int(numeros[1])

print(mdc(num1, num2))
