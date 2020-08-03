import datetime
monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
def date_validation(day, month, year): 
    valid=True
    try : 
        datetime.datetime(int(year),int(month), int(day))
    except ValueError : 
        valid= False
    return valid
def countLeapYears(d,m,y): 
    years = y
    if (m <= 2) : 
        years-= 1
    return int(years / 4 - years / 100 + years / 400 ) 
def getDifference(d1,m1,y1,d2,m2,y2): 
    n1 = y1 * 365 + d1 
    for i in range(0, m1 - 1): 
        n1 += monthDays[i]
    n1 += countLeapYears(d1,m1,y1)
    n2 = y2 * 365 + d2 
    for i in range(0, m2 - 1): 
        n2 += monthDays[i]  
    n2 += countLeapYears(d2,m2,y2)
    return (n2 - n1)
#Mystery Of Sky
d1,m1,y1=1,1,1
day=input()
try:
    d2,m2,y2=map(int,input().split('/'))
    if(not date_validation(d2,m2,y2)):
        print("Invalid Date")
    else:
        n=getDifference(d1,m1,y1,d2,m2,y2)
        days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        ind=days.index(day)
        if(n%4==3 or (ind+n)%7==5 or (ind+n)%7==6):
            print(0)
        else:
            n=getDifference(0,1,y2,d2,m2,y2)
            print(min(n,50))
except:
    print("Invalid Day")