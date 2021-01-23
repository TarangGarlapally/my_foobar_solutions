import math

def solutionWithoutFloor(n):
    sum_of_n = n*(n+1)//2
    return sum_of_n*(math.sqrt(2))

def extraNums(start,end):
    #print(start,end)
    redundant = 0
    extras = 0
    #print(start,end)
    for i in range(start,end+1):
        a = i*math.sqrt(2)
        redundant = a - math.floor(a)
        extras += redundant


    return extras


def solution2(s):
    n = int(s)
    res = 0


    for i in range(1,n+1):
        res += math.floor(i*math.sqrt(2))

    return str(int(res))

def solution(s):
    #calculate result without floor
    n = int(s)
    result = solutionWithoutFloor(n)


    #has a pattern of 70, for each multiple of 70, there are 35 extra 1's
    #calculate by bruteforce after 70 multiples end
    start = n//3832  # 70
    extras = start*(10384108) #35
    start = (start*3832) + 1
    #print(extras)
    extras += extraNums(start,n) #inclusive
    #print(extras)
    result = math.floor(result - extras)
    return str(int(result))


q = "293"
print(solution(q), solution2(q))

cnt=0
for i in range(1,1000):
    if(solution(i) != solution2(i)):
        print(i,solution(i), solution2(i))
        cnt += 1
print(cnt)

