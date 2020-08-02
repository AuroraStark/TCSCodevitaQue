'''
1 full triangle

full triangle
n+1 rows

n - 2 partial triangles
partial triangle n-1
    n-1 rows
partial triangle n-2
    n-2 rows
upto
partial triangle
    2 rows
stand
'''
for _ in range(int(input())):
    n=int(input())
    if(n<=1):
        print("You cannot generate christmas tree")
    elif n>20:
        print("Tree is no more")
    else:
        print(" "*n+"*")
        for i in range(1,n):
            for j in range(1,(n-i)+2):
                print(" "*(n-j)+"*"*((j*2)+1))
        print(" "*n+"*")
        print(" "*n+"*")