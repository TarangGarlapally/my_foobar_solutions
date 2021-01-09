# learned about maximum corridor problem

#ford fulkerson algorithm
def minSteps(path, s, n):
    pred = [-1 for i in range(n)]
    d_from_s = path[s][:]
    for i in range(n):
        if(d_from_s[i] != 0):
            d_from_s[i] = 1
            pred[i] = s
        else:
            d_from_s[i] = 200000

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


    if(pred[-1]==-1):
        return -1
    
    d = 2000000
    l=[]
    curr_node = n-1
    l.append(curr_node)
    while curr_node!=s:
        node = curr_node
        curr_node = pred[curr_node]
        l.append(curr_node)
        if(path[curr_node][node]!=0 and path[curr_node][node]<d):
            d = path[curr_node][node]
        
    return [d,l]


def solution(entrances, exits, path):
    n = len(path)
    c = 0
    
    bunnies_reached = 0

    #connect all entrances to a new node(start node), and all exits to another new node(end)
    #add all outgoing paths from entrances and put them in corresponding slots in start node
    #add all incoming paths to exits and put them in corresponding slots in end node
    for i in range(n):
        path[i].append(0)
        if(i not in exits):
            path[i].append(0)
        else:
            x = 0
            for j in range(n):
                x+=path[j][i]
            path[i].append(x)
    l=[0 for i in range(n+2)]
    for entrance in entrances:
        l[entrance] = sum(path[entrance])
    path.append(l)
    path.append([0 for i in range(n+2)])

    #check if path exits from source to destination nodes, if yes get the path and also the bunny capacity of the path
    s_to_d = minSteps(path,n,n+2)

    #while path exists, calculate residual bunnies at each edge in the path and create back edges which could be later used to send back bunnies to not cross capacity
    #add capacity to bunnies_reached
    while(s_to_d != -1):
        min_bunnies = s_to_d[0]
        s_to_d = s_to_d[1]
        s_to_d.reverse()

        bunnies_reached += min_bunnies

        for i in range(len(s_to_d)-1):
            path[s_to_d[i]][s_to_d[i+1]] -= min_bunnies
            path[s_to_d[i+1]][s_to_d[i]] += min_bunnies
        
        s_to_d = minSteps(path,n,n+2)
 
    
    return bunnies_reached



print(solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))



