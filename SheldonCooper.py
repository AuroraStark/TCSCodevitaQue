def pairwisesolve(n,q,x,i):
    low,high = i,n-1
    while low<high:
        if q[low]+q[high]<x:
            low +=1
        elif q[low]+q[high]>x:
            high -=1
        else:
            return True
    return False
def solve(n,q,x):
    sorteddq = sorted(q)
    for i in range(n-2):
        if pairwisesolve(n,sorteddq,x-sorteddq[i],i+1):
            return True
    return False
n = int(input())
q = [int(input()) for _ in range(n)]
x= int(input())
print(solve(n,q,x))
    




