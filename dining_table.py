import math
def comb(n,r):
    if n==r or r==0:
        return 1
    if r==1:
        return n
    res=math.factorial(n)//math.factorial(r)
    res=res//math.factorial(n-r)
    return res
for _ in range(int(input())):
    r,n=map(int,input().split(' '))
    a,b=n//r,n%r
    p1,p2=a+1,a
    cmbs=1
    for i in range(b):
        cmbs=cmbs*comb(n,p1)
        n=n-p1
    for i in range(b,r):
        cmbs=cmbs*comb(n,p2)
        n=n-p2
    print(cmbs)