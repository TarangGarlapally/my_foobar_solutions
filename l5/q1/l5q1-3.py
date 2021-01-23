import math
def solution(s):
    n = int(s)
    sumOfN = n*(n+1)/2
    res = sumOfN*(math.sqrt(2))
    print(n*math.sqrt(2))
    
    res -= (n/2)

    res = math.floor(res)
    return str(int(res))

def solution2(s):
    n = int(s)
    res = 0


    for i in range(1,n+1):
        res += math.floor(i*math.sqrt(2))

    return str(int(res))
l=[]
m=[]
odd = []
even = []

cnt=0
'''for i in range(1,1000):
    if(solution(i) != solution2(i)):
        print(i,solution(i), solution2(i))
        cnt += 1
print(cnt)
# should not substract -1 for 1, 2, 3, 4, 5, 7, 9, 11, 12, 13, 14, 15, 16, 17, 19, 21, 23, 24, 25, 26, 27, 28, 29, 31, 33, 37, 39, 41, 42, 43, 44, 45,       
# should substract -1 for 6, 8, 10, 18, 20, 22, 30, 32, 34, 35, 36, 38, 40, 46, 52, 58, 62, 64, 66, 68, 76, 100, 102, 104, 110, 116, 122, 128, 132, 134 
q = "5"
print(l)
print(m)
print(len(odd), len(even), odd, even)
'''
q="1000"
print(solution(q),solution2(q))
for i in range(1,21):
    print(i,solution(i),solution2(i))
#print(solution2(q))
