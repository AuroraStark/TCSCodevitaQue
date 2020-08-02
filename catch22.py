#ctach 22 
for _ in range(int(input())):
    p = list(input().split())
    s = 'F'
    fos,bas,d,fob,bab = list(map(int,p[:]))
    cu,pos = 0,0
    re = 0    
    if fos == bas:
        if s == 'F' and fob<=fos:
            print(fob*d,'F')
        elif s == 'B' and bab<=bas:
            print(bab*d ,'B')
        else:
            print('No Ditch')
        continue
    if pos+fos >= fob and s == 'F':
        re += fob*d
        print(re,'F')
        continue
    if pos+bas >= bab and s == 'B':
        re += bab*d
        print(re,'B')
        continue
    if fos > bas:
        a,b,t = fos,bas,fob
        flag = 'F'
        if s == 'B':
            re += bas*d
            cu = cu-bas
    else:
        a,b,t = bas,fos,bab
        flag ='B'
        if s == 'F':
            re += fos*d
            cu = cu-fos
    while(cu+a < t):
        re += (a+b)*d
        cu += (a-b)
    re += (t-cu)*d       
    print(re,flag)