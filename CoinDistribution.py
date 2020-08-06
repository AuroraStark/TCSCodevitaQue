

first_ten=[[0,0,1],[0,0,2],[0,1,1],[0,1,2],[0,2,1],[0,2,2],[0,3,1],[0,3,2],[1,1,2],[1,2,1]]
n=int(input())
if(n<10):
    print(sum(first_ten[n-1]),end=' ')
    for i in first_ten[n-1]:
        print(i,end=' ')
else:
    if(n%10 == 0):
        counter_five = (n-10)//5
        config = first_ten[9]
        config[0]+= counter_five
    elif(n%10 < 5):
        counter_five = (n-(n%10)-5)//5
        config = first_ten[n%10+5-1]
        config[0]+= counter_five
    elif(n%10>=5):
        counter_five = (n-(n%10))//5
        config = first_ten[n%10-1]
        config[0]+= counter_five
    print(sum(config),end=' ')
    for i in config:
        print(i,end=' ')


