#exam efficiency
x1=int(input())
x2=int(input())
x3=int(input())
y=int(input())
if x2*2+x3*3>=y:
    print('One mark question need not be attempted, so no minimum accuracy rate applicable')
else:
    diff = y-(x2*2+x3*3)
    m=(diff+x1)/2
    res=100*m*(1/x1)
    p=str(res).split('.')
    if p[1]=='0':
        print('Minimum Accuracy rate required for One mark question is '+str(int(res))+'%')
    else:
        print('Minimum Accuracy rate required for One mark question is '+str(round(res,2))+'%')
if x1*1+x3*3>=y:
    print('Two mark question need not be attempted, so no minimum accuracy rate applicable')
else:
    diff = y-(x1*1+x3*3)
    m=(diff+2*x2)/4
    res=100*m*(1/x2)
    p=str(res).split('.')
    if p[1]=='0':
        print('Minimum Accuracy rate required for Two mark question is '+str(int(res))+'%')
    else:
        print('Minimum Accuracy rate required for Two mark question is '+str(round(res,2))+'%')
if x2*2+x1*1>=y:
    print('Three mark question need not be attempted, so no minimum accuracy rate applicable')
else:
    diff = y-(x2*2+x1*1)
    m=(diff+3*x3)/6
    res=100*m*(1/x3)
    p=str(res).split('.')
    if p[1]=='0':
        print('Minimum Accuracy rate required for Three mark question is '+str(int(res))+'%')
    else:
        print('Minimum Accuracy rate required for Three mark question is '+str(round(res,2))+'%')