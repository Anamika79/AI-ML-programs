from queue import PriorityQueue
import math

def a_star_search(graph,start,goal):
    queue = PriorityQueue()
    start_h = heuristic(coordinates[start],coordinates[goal])
    queue.put((start_h,0,[start],start))

    visited = set()

    while not queue.empty():
        (f_score,g_cost,path,node) = queue.get()
        if node == goal:
            return path,g_cost
        if node in visited:
            continue
        visited.add(node)

        for next_node,next_cost in graph[node].items():
            new_g_cost = g_cost + next_cost
            h_n = heuristic(coordinates[next_node],coordinates[goal])
            f_score =   new_g_cost + h_n

            queue.put((f_score,new_g_cost,path + [next_node] , next_node))

    return None

def heuristic(node,goal):
    x1,y1 = node
    x2,y2 = goal
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


graph = {
    'S':{'A':1},
    'A':{'B':2,'D':2},
    'B':{'C':1},
    'C':{'G':2},
    'D':{'G':4},
    'G':{}
}

coordinates = {
    'A': (1, 0),
    'B': (2, 0),
    'C': (3, 0),
    'D': (2, -1),
    'G': (5, 0),
    'S': (0, 0)
}

path,total_cost = a_star_search(graph,'S','G')
print("Path : ", path)
print("Total cost : ",total_cost)