def solution(times, times_limit):
    curr_node = 0
    nbunnies = len(times)-2
    length = nbunnies+2
    saved = []
    while(curr_node != length-1 or times_limit != 0):
        if(curr_node != length-1 and times[curr_node][length-1] == -1):
            curr_node = length - 1
            times_limit += 1
        elif(curr_node != length-1 and times_limit == times[curr_node][length-1]):
            curr_node = length - 1
            times_limit -= times[curr_node][length-1]
            break
        else:
            temp_node = times[curr_node][1:].index(min(times[curr_node][1:curr_node]+times[curr_node][curr_node+1:length-1]))+1
            temp_time = times[curr_node][temp_node]
            prev_node = curr_node
            times_limit -= temp_time; curr_node = temp_node
            if(curr_node!=0):
                saved.append(curr_node-1)
            times[prev_node][curr_node] = 1000
    
    saved.sort()
    return saved

print(solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3))
    

