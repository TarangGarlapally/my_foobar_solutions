import math
def solution(s):
    n = int(s)
    sumOfN = n*(n+1)//2
    res = sumOfN + sumOfN*(math.sqrt(2)-1)

    if(n%2==0):
        res -= (n//2)-1
    else:
        res -= (n//2)
    res = math.floor(res)
    return str(res)



print(solution("10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"))

print(10**100)
