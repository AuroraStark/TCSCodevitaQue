#Televison sets TCS Codevita
def calculate(n,k,l,r1,r2):
    res=0
    for i in range(1,len(l)):
        if i<=(n-k):
            res+=l[i]*i*r2
        else:
            a=n-k
            b=i-a
            res=res+(a*l[i]*r2)+(b*l[i]*r1)
    return res

n=int(input())
r1,r2=map(int,input().split(' '))
t=int(input())
d=[0,31,28,31,30,31,30,31,31,30,31,30,31]
r=[0]*(min(53,n+1))
for i in range(1,13):
    for j in range(1,d[i]+1):
        a=(6-i)**2+abs(j-15)
        k=min(a,n)
        r[k]+=1
total=0
flg=False
res=0
for i in range(n+1):
    rev=calculate(n,i,r,r1,r2)
    if rev>=t:
        flg=True
        res=i
        break
if flg:
    print(res)
else:
    print(n)