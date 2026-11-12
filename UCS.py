from queue import PriorityQueue

def uniform_cost_search(graph,start,goal):
    queue = PriorityQueue()
    queue.put((0,[start],start))

    visited = set()

    while not queue.empty():
        node_cost,path,node = queue.get()

        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            return path,node_cost
        
        #check for neighbors
        for next_node,next_cost in graph[node].items():
            if next_node not in visited:
                new_cost = node_cost + next_cost
                queue.put((new_cost, path+[next_node] , next_node))
            
    return None,None


# Creating a graph
def create_graph():
 graph = {
 'arad': {'zerind': 75, 'timisoara': 118, 'sibiu': 140},
 'zerind': {'oradea': 71, 'arad': 75},
 'timisoara': {'lugoj': 111, 'arad': 118},
 'sibiu': {'fagaras': 99, 'oradea': 151, 'arad': 140,
 'rimnicuvilcea': 80},
 'oradea': {'zerind': 71, 'sibiu': 151},
 'fagaras': {'sibiu': 99, 'bucharest': 211},
 'bucharest': {'fagaras': 211, 'pitesti': 101,
 'urziceni': 85, 'giurgiu': 90},
 'pitesti': {'rimnicuvilcea': 97, 'bucharest': 101,
 'craiova': 138},
 'urziceni': {'bucharest': 85, 'hirsova': 98, 'vaslui': 142},
 'giurgiu': {'bucharest': 90},
 'rimnicuvilcea': {'sibiu': 80, 'pitesti': 97, 'craiova': 146},
 'craiova': {'rimnicuvilcea': 146, 'pitesti': 138, 'drobeta': 120},
 'hirsova': {'eforie': 86, 'urziceni': 98},
 'vaslui': {'urziceni': 142, 'iasi': 92},
 'drobeta': {'mehadia': 75, 'craiova': 120},
 'eforie': {'hirsova': 86},
 'iasi': {'vaslui': 92, 'neamt': 87},
 'mehadia': {'lugoj': 70, 'drobeta': 75},
 'neamt': {'iasi': 87},
 'lugoj': {'timisoara': 111, 'mehadia': 70}
 }
 return graph

graph = create_graph()
path,cost = uniform_cost_search(graph,"zerind","bucharest")

if path:
    print("UCS path : ",path)
    print("UCS path cost : ",cost)
else:
    print("No path found")