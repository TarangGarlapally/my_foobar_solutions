from collections import deque 
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
        for i in range(n):
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
        
        




print(solution([0, 1], [4, 5], [[0, 0, 4, 9, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 3], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
