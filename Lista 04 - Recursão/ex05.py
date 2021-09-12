listaNum = []
def quadPerf(num):
    if num > 1:
        listaNum.insert(0, num)
        analisado = quadPerf(num - 2)
        listaNum.pop(0)
        if len(listaNum) > 0:
            print(f"{num} + soma({listaNum})")
        else:
            print(f"{num}")
        return analisado + num
    else:
        if len(listaNum) > 0:
            print(f"{num} + soma({listaNum})")
        else:
            print(f"{num}")
        return 1

num = int(input())
total = quadPerf(2*num-1)
print("---------------")
print(f"{num} ** 2 == {total}")