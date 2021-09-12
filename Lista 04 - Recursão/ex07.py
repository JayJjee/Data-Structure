cont = 0
def Fib(n):
    global cont
    cont += 1
    if n<=1:
        return n
    else:
        return Fib(n-1)+Fib(n-2)

n = int(input())
print(f'Fib({n}) = {Fib(n)} ({cont} chamadas)')