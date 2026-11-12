from queue import PriorityQueue

def best_first_search(graph,start,goal,heuristic):
    queue = PriorityQueue()
    queue.put((heuristic[start],[start],start))

    visited = set()
    while not queue.empty():
        priority,path,node = queue.get()

        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            return path

        for next_node,next_cost in graph[node].items():
            if next_node not in visited:
                queue.put((heuristic[next_node],path+[next_node],next_node))
        
    return None

# Graph representation
graph = {
 'A': {'B': 2, 'C': 4},
 'B': {'D': 3, 'E': 5},
 'C': {'F': 2},
 'D': {'G': 4},
 'E': {'G': 2},
 'F': {'G': 3},
 'G': {}
}
# Heuristic values
heuristic = {
 'A': 7,
 'B': 6,
 'C': 4,
 'D': 5,
 'E': 3,
 'F': 2,
 'G': 0
}

path = best_first_search(graph,'A','G',heuristic)
print(path)