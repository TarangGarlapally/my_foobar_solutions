'''import math
i=0
#Beatty Sequence
def sumOfN(n):
    return n*(n+1)//2
def solution2(s):
    n = int(s)
    res = 0


    for i in range(1,n+1):
        res += math.floor(i*math.sqrt(2))

    return str(int(res))
def beattySeqSum(n):
    global i
    i+=1
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    elif(n == 2):
        return 3
    x = math.floor((math.sqrt(2)-1)*n)
    res = n*x + sumOfN(n) - sumOfN(x) - beattySeqSum(x)
    return res

def solution(s):
    n = int(s)
    return str(int(beattySeqSum(n)))

print(solution("5"))
#print(i)

for i in range(1,100):
    print(solution2(str(i)))

'''


#Beatty Sequence

def sumOfN(n):
    return (n*(n+1)//2)
    
def beattySeqSum(n):
    #floating point multiplications errors occur as computers are not perfect at floating point multiplication, so convert to integer by multiplying with 10**!00
    sqrt2 = 14142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727
    if(n < 1):
        return 0
    elif(n == 1):
        return 1
    elif(n == 2):
        return 3
    #no math.floor instead using integer division 
    x = ((sqrt2 - 10**100)*n//10**100)
    res = n*x + sumOfN(n) - sumOfN(x) - beattySeqSum(x)
    return res

def solution(s):
    n = int(s)
    return str(beattySeqSum(n))
print(solution("77"))
