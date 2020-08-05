
for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    #print(minproduct(a,b,n,k))
    ori_sum=0
    for i in range(n):
        ori_sum+=a[i]*b[i]
    new_sum = ori_sum
    for i in range(n):
        curr_prod = a[i]*b[i]
        select_pro = min((a[i]+2*k)*b[i],(a[i]-2*k)*b[i])
        temp_sum=ori_sum - curr_prod+select_pro
        if temp_sum<new_sum:
            new_sum = temp_sum
    print(new_sum)



