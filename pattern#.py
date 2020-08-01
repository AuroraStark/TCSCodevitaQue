# if n=3 then pattern will be 10203010011012**4050809***607
t=int(input())
for _ in range(t):
    n=int(input())
    m=n*(n+1)
    k=m
    l=[]
    end=n
    start=0
    a=0
    print("Case #"+str(_+1))
    for i in range(1,m+1):
        l.append(str(i))
    for i in range(n):
        print("*"*a,end="")
        print("0".join(l[:end]),end="0")
        print("0".join(l[-end:]))
        l=l[end:k-end]
        k=len(l)
        end=end-1
        a+=2