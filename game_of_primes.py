'''
Game Of Primes
5 = 2 + 3
17 = 2 + 3 + 5 + 7
41 = 2 + 3 + 5 + 7 + 11 + 13
'''
def getPrime(n):
    isprime=[False,False]+[True]*(n-1)
    factor=2
    primes=list()
    while factor<=n:
        if isprime[factor]:
            primes.append(factor)
            for i in range(factor*factor,n+1,factor):
                isprime[i]=False
        factor+=1
    return primes
q=list()
for _ in range(int(input())):
    q.append(int(input()))
res=list()
primes=getPrime(max(q))
#print(primes)
s=2
for i in range(1,len(primes)):
    s+=primes[i]
    if s in primes:
        res.append(s)
for i in q:
    print(len([j for j in res if j<=i]))