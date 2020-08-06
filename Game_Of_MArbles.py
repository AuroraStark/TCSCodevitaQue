import math
def lcm(nums):
    a=nums[0]
    b=nums[1]
    cur_lcm=(a*b)//math.gcd(a,b)
    for i in nums[2:]:
        cur_lcm=(cur_lcm*i)//math.gcd(cur_lcm,i)
    return cur_lcm
try:
    n=int(input())
    n=n//2
    d={"Sally":0,"Darrell":0}
    for case in range(n):
        que_input=input().split()
        questioner=que_input[0]
        nums_str=que_input[1]
        nums=list(map(int,nums_str.split(',')))
        assert(2<=len(nums)<=7)
        for nu in nums:
            assert(1<=nu<=100)
        #print(questioner,nums)
        correct_ans=lcm(nums)
        print(f"{questioner}'s question is : {nums_str}")
        ans_input=input().split()
        answerer=ans_input[1]
        if case==0:
            fquestioner=questioner
            fanswerer=answerer
        if ans_input[2]!='PASS':
            ans=int(ans_input[2])
            if ans==correct_ans:
                print('Correct Answer')
                print(f'{answerer}: 10points')
                d[answerer]=d[answerer]+10
            else:
                print('Incorrect Answer')
                print(f'{answerer}: 0points')
        else:
            print('Question is PASSed')
            print("Answer is: {}".format(correct_ans))
            print(f"{answerer}: 0points")
        if case==n-1:
            print('Total Points:')
            print(f'{fquestioner}: {d[fquestioner]}points')
            print(f'{fanswerer}: {d[fanswerer]}points')
            if d['Sally']==d['Darrell']:
                print('Game Result: Draw')
            else:
                winner='Sally' if d['Sally']>d['Darrell'] else 'Darrell'
                print(f'Game Result: {winner} is winner')
except:
    print("Invalid Input")




