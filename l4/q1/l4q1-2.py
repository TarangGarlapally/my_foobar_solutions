def solution(times, times_limit):
    curr_node = 0
    nbunnies = len(times)-2
    length = nbunnies+2
    negatives = 0
    result = []
    temp_result = []


    
    for row in times:
        for ele in row:
            if(ele<0):
                negatives += ele
    while(times_limit >= negatives):
        if(times_limit == times[curr_node][-1] and negatives == 0):
            times_limit -= times[curr_node][-1]
            curr_node = length-1
            break
        temp_id = 0

        temp_list = times[curr_node][1:curr_node]+times[curr_node][curr_node+1:]
        temp_id = times[curr_node][1:].index(min(temp_list)) + 1
            
        times_limit -= times[curr_node][temp_id]
        prev_node = curr_node
        curr_node = temp_id
        if(curr_node != 0 and curr_node != length-1):
            temp_result.append(curr_node - 1)
            times[prev_node][curr_node] = 2147483647
        if(curr_node == length-1 and times_limit >= 0):
            result = temp_result[:]
    if(curr_node == length-1 and times_limit >= 0):
            result = temp_result[:]
    result = list(set(result))
    result.sort()
    return result


print(solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1))
    

