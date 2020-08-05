n = int(input())
ls = list(map(int,input().split()))
if n%2==1:
    print("AMAN")
else:
        res = 0
        for num in ls:
            res = (res^num)
        if res != 0:
            print("AMAN")
        else:
            print("JASBIR")
