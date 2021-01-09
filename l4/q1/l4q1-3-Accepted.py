#using single source shortest path (Bellman ford) and find all possibilities
def shortestPaths(source_map, s, n):
    d_from_s = source_map[s]

    def newD(node):
        for i in range(n):
            if(i != node):
                if(d_from_s[i] + source_map[i][node] < d_from_s[node]):
                    d_from_s[node] = d_from_s[i] + source_map[i][node]

    for i in range(n-1):
        for j in range(n):
            if(s != j):
                newD(j)
    return d_from_s
    



def solution(times, times_limit):
    length = len(times)
    nbunnies = length - 2
    s = 0
    d = shortestPaths(times, s, length)
    result = [[]]

    def exploreBunnies(di, i, time_left, temp_result):
        d_from_i = shortestPaths(times, i, length)
        if(di+d_from_i[-1]<=times_limit):
            result.append(temp_result)

        if(len(temp_result) == nbunnies):
            return
        
        for bunny in range(1, nbunnies+1):
            if(bunny not in temp_result):
                exploreBunnies(di+d_from_i[bunny],bunny, time_left - d_from_i[bunny], temp_result + [bunny])
        
    for i in range(1, nbunnies+1):
        temp_result = [i]
        exploreBunnies(d[i], i, times_limit, temp_result)

    result.sort(key = lambda x: -len(x))
    for i in range(len(result[0])):
        result[0][i] -= 1
    result[0].sort()
    return result[0]




case = [[0, 10, 10, 1, 10],
              [10, 0, 10, 10, 1],
              [10, 1, 0, 10, 10],
              [10, 10, 1, 0, 10],
              [1, 10, 10, 10, 0]]

print(solution(case, 6))
    
