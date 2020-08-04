for _ in range(int(input())):
    x=int(input())
    y=int(input())
    va=int(input())
    vb=int(input())

    min_distance=((x*x)+(y*y))**0.5  
    while(x>=0 or y>=0):
        x=x-va
        y=y-vb
        distance=((x*x)+(y*y))**0.5
        min_distance=min(min_distance,distance)
    if min_distance==0.0:
        print(0.0)
    else:
        print(format(min_distance,".11f"))
