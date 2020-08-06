n = int(input())
der = [0 for _ in range(n+1)]
der[0],der[1],der[2] = 1,0,1
d = 1000000007
for i in range(3,n+1):
    der[i] = ((i-1)*(der[i-1]+der[i-2]))%d
print(der[n]%d)
    
    




