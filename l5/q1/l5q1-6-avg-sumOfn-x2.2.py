import math
from scipy.integrate import quad
def solution(s):
    n = int(s)
    sum_of_n = n*(n+1)/2.0
    a = ((n*n)/2.0)*math.sqrt(2)
    b = sum_of_n*math.sqrt(2) #sumof5n
    return str(int(math.floor((a+b)/2)))
#error increases from 1 to n in the above case
    

def solution2(s):
    n = int(s)
    ans = math.floor((n*n)/2.0) + math.floor(n/(2.0*math.sqrt(2)))
    
    return str(int(ans*math.sqrt(2)))


print(solution2("77"))
print((300*300))
