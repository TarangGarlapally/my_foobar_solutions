import math
l=[]

def solution2(s):
    n=int(s)
    sumOfN = n*(n+1)//2
    sm = sumOfN
    sm += sumOfN*(math.sqrt(2)-1)
    return sm

def solution(s):
    n = int(s)
    res = 0
    sm = 0

    for i in range(1,n+1):
        res += math.floor(i*math.sqrt(2))
        sm +=  math.floor(i*math.sqrt(2))
        if(i%7==0):
            l.append(sm)
            sm=0

    return str(res),n*(n+1)//2
a,b = solution("77")
print(a,b,int(a)-b)
print((b)*(math.sqrt(2)-1))
print(77*math.sqrt(2))
print(solution2("77")-int(a))
print(l)
z=[]
for i in range(len(l)-1):
    z.append(l[i+1]-l[i])
print(z)
print(len(z))
print(set(z))
print("68:", z.index(68),list(reversed(z)).index(68))
print("69:", z.index(69),list(reversed(z)).index(69))
print("70:", z.index(70),list(reversed(z)).index(70))
