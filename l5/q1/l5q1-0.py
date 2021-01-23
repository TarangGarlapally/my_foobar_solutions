import math
def solution(s):
    n = int(s)
    res = 0


    for i in range(1,n+1):
        res += math.floor(i*math.sqrt(2))

    return str(int(res))


print(solution("1000"))
