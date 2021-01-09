'''
from collections import deque
from itertools import combinations
def solution(l):
    length = len(l)
    if(length<3):
        return 0
    count = 0
    for x in list(map(list,combinations(l,3))):
        if(x[1]%x[0] == 0 and x[2]%x[1] == 0):
            count+=1
    return count

print(solution([1,1,2,2,4,4]))
'''

def solution(l):
    length = len(l)
    if(length<3):
        return 0
    count = 0
    for i in range(1,length-1):
        counta = 0
        for m  in range(0, i):
            if(l[i]%l[m] == 0):
                counta+=1
        countb = 0
        for n  in range(i+1,length):
            if(l[n]%l[i] == 0):
                countb+=1
        count += counta*countb
    return count




print(solution([1,2,3,4,5,6]))
