def solution(entrances, exits, path):
    n = len(path)
    l = [0 for i in range(n)]
    for entrance in entrances:
        for i in range(n):
            if(path[entrance][i] != 0):
                l[entrance]+=path[entrance][i]
    total_bunnies = 0
    for ps in range(n):
        ltemp = [0 for i in range(n)]
        for i in range(n):
            for j in range(n):
                if(l[j] != 0 and path[j][i] != 0 and i != j):
                    if(path[j][i]<=l[j]):
                        ltemp[i] += path[j][i]
                        l[j] -= path[j][i]
                        
                    else:
                        ltemp[i] += l[j]
                        l[j] = 0
        for each_exit in exits:
            total_bunnies += ltemp[each_exit]
            ltemp[each_exit] = 0

        l = ltemp[:]
        
    

    return total_bunnies




print(solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
