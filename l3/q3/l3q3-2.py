from collections import deque
def solution(l):
    length = len(l)
    if(length<3):
        return 0
    count = 0
    for i in range(length-2):
        stack = deque()
        stack.append(l[i])
        j = i+1
        while(j<length-1):
            if(l[j]%stack[-1]==0):
                stack.append(l[j])
                k = j+1
                while(k<length):
                    if(l[k]%stack[-1]==0):
                        count += 1
                        print(l[i],l[j],l[k])
                    k += 1
                stack.pop()
            j += 1
        stack.pop()
    return count

print(solution([1,1,2,2,4,4]))
