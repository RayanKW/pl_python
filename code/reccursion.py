#fibonacci sequence
def fibo(n):
    if n<=0:
        return n
    elif n == 1:
        return 1
    else:
        return fibo(n - 2) + fibo(n - 1)
print(fibo(9))