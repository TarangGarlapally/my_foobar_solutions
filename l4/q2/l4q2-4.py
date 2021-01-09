from collections import deque 

def minSteps(path, s, n, exits):
    pred = [-1 for i in range(n)]
    d_from_s = path[s][:]
    for i in range(n):
        if(d_from_s[i] != 0):
            d_from_s[i] = 1
        else:
            d_from_s[i] = 0

    def newD(node):
        for i in range(n):
            if False if path[i][node]==0 else True :
                if(d_from_s[i]+1  <d_from_s[node]):
                    d_from_s[node] = d_from_s[i]+1
                    pred[node] = i

    for i in range(n-1):
        for j in range(n):
            if(s != j):
                newD(j)

    d = 2147483647
    for x in exits:
        if(d_from_s[x]<d):
            d = d_from_s[x]
    
    return d


def solution(entrances, exits, path):
    n = len(path)
    c = 0
    queue = deque()

    bunnies_at_node = [0 for i in range(n)]

    
    for entrance in entrances:
        bunnies_at_node[entrance] = sum(path[entrance])
        queue.append([entrance,0])
    
    ps = 0
    
    while(queue):
        node = queue.popleft()
        if(ps != node[1]):
            if c>0:
                break
        
        ps = node[1]
        node = node[0]

        d_lst = []
        for i in range(n):
            x = path[node][i]
            temp = 0
            if(x != 0):
                d_lst.append([i,minSteps(path, i, n, exits)])
        d_lst.sort(key = lambda x: x[1])
        
        for j in d_lst:
            i = j[0]
            x = path[node][i]
            temp = 0
            if(x != 0):
                if(x<bunnies_at_node[node]):
                    bunnies_at_node[i] += x
                    bunnies_at_node[node] -= x
                    temp = x
                else:
                    bunnies_at_node[i] += bunnies_at_node[node]
                    temp =  bunnies_at_node[node]
                    bunnies_at_node[node] = 0

                if([i,ps+1] not in queue):
                    queue.append([i,ps+1])
            if(i in exits):
                c += temp
        
    return c
        
        




print(solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]))
