def maxBunniesPossible(path,s,n):
    bunnies_from_s = path[s]
    def newBunnies(node):
        for i in range(n):
            if(i != node):
                if(min(bunnies_from_s[i],path[i][node]) > bunnies_from_s[node]):
                    bunnies_from_s[node] = min(bunnies_from_s[i],path[i][node])
    for i in range(n-1):
        for j in range(n):
            if(s != j):
                newBunnies(j)
    return bunnies_from_s

def solution(entrances, exits, path):
    n = len(path)
    c = 0
    for entrance in entrances:
        for i in range(n):
            if path[entrance][i] != 0:
                bunnies_from_s = maxBunniesPossible(path,i,n)
                for exitnode in exits:
                    b = min(path[entrance][i],bunnies_from_s[exitnode])
                    path[entrance][i] -= b
                    c += b
    return c




print(solution([0, 1], [4, 5], [[0, 0, 4, 9, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 3], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
