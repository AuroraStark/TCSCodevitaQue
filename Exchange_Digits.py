#Exchange Digits
from itertools import permutations
a,b = map(int,input().split())
a = list(str(a))
flag = False
perm = permutations(a)
perm = sorted(perm)
for i in list(perm):
    s="".join(list(i))
    if s[0]!='0' and int(s)>b:
        flag = True
        break
if flag==True:
    print(s)
else:
    print("-1")
        



