import math
import heapq as h

def reconstruct_path(cameFrom, current):
    path = []
    total_path = [current]
    while current in cameFrom:
        current = cameFrom[current]
        total_path.append(current)     
    return total_path

# Function to calculate distance
# def distance(start, end):
#      return math.hypot(end[0] - start[0], end[1] - start[1])
#     return math.sqrt((start[0] - end[0]) ** 2 + (start[1] - end[1]) ** 2)

def heuristic_distance(M, startnode, endnode):
    abs_diff_x_square = math.pow((M.intersections[startnode][0] - M.intersections[endnode][0]),2)
    abs_diff_y_square = math.pow((M.intersections[startnode][1] - M.intersections[endnode][1]),2) 
    distance_bet_nodes = math.sqrt(abs_diff_x_square + abs_diff_y_square)
    return distance_bet_nodes


def Astar(M,start,goal):
    closedSet = set([])
    openSet = set([start])
    cameFrom = {}
    paths  = list(M.intersections.keys())
    
    G = {road : float("inf") for road in paths}
    G[start] = 0
    F = {road: float("inf") for road in paths}
    F[start] = heuristic_distance(M,start,goal)
    frontier = [(F[start], start)]

    while openSet:
        current = h.heappop(frontier)

        if current[1] == goal:
            reversepath = reconstruct_path(cameFrom, current[1])
            reversepath.reverse()
            print(reversepath)
            return reversepath
        
        if current[1] in openSet:    
            openSet.remove(current[1])
            closedSet.add(current[1])
        
        for i in M.roads[current[1]]:
            if i in closedSet:
                continue
                
            if i not in openSet:
                openSet.add(i)
            
            tentative_G = G[current[1]] + heuristic_distance(M, current[1], i)
            if tentative_G >= G[i]:
                continue
                
            cameFrom[i] = current[1]
            G[i] = tentative_G
            F[i] = (G[i] + heuristic_distance(M, i, goal))
            h.heappush(frontier, (F[i], i))
       
    return ("Failed function")

def shortest_path(map, start,end):
    M = map
    S = start
    goal = end
    # print(type())
    result = Astar(M, S, goal)
    # print(result)
    return result
