from itertools import permutations
n=int(input())
l=list(map(int,input().split()))
l.sort()
l=l[-6:]
per=permutations(l)
res=[]
for ele in per:
    l1=list(ele)
    l=[]
    for k in range(4):
        for i in range(len(l1)-1):
            l.append(l1[i]+l1[i+1])
        l1=l
        l=[]
    res.append(l1[0]*l1[1])
print(max(res))




