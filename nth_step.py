#1 step or 2 step or 3 step
d = 1000000007
def fibo(n):
    if n<=2:
        return fib_array[n]
    for i in range(3,n+1):
        fib_array.append((fib_array[-1]+fib_array[-2])%d)
    return fib_array[-1]
fib_array = [1,1,2]
n = int(input())
instep=fibo(n)
outstep=0
for i in range(3,n+1):
    temp = n-i
    tempres = (fib_array[n-(temp+3)]*fib_array[temp])%d
    onestep = tempres
print((instep+onestep)%d)