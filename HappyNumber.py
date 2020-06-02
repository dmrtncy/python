
# Happy number

def ishappy(num):
    numtemp = num
    set_sum = set()
    sum = 0
    result=0
    while True:
        str_num = str(numtemp)
        for i in str_num:
            sum = sum + (int(i)**2)
        if sum in set_sum:
            result=False
            break
        elif sum==1:
            result=True
            break
        set_sum.add(sum)
        numtemp = sum
        sum = 0
    return result
"""
for i in range(50):
    if ishappy(i):
        print(i,"is a happy number")
    else:
        print(i,"is not a happy number")
"""