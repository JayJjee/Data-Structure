dic = {0: 0}
def fibonacci(n):
    if n<=1:
        if n not in dic:
            dic[n] = 1
        else:
            dic[n] += 1
        return n
    else:
        fib = fibonacci(n-1)+fibonacci(n-2)
        if n not in dic:
            dic[n] = 1
        else:
            dic[n] += 1
        return fib

n = int(input())
print(f"fibonacci({n}) = {fibonacci(n)}.")
for valorFib, qntFib in dic.items():
    print(f"{qntFib} chamada(s) a fibonacci({valorFib}).")