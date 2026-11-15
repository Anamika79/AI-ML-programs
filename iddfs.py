def iddfs(graph,start,goal,limit,path=None):
    if path is None:
        path = []
    path = path + [start]

    if start == goal:
        return path
    if start not in graph:
        return None
    if limit == 0:
        return None

#for neighbor in reversed(list(graph[start].keys())):  -->if need to work like stack
    for neighbor in graph[start].keys():
        if neighbor not in path:
            new_path = iddfs(graph,neighbor,goal,limit-1,path)

            if new_path is not None:
                return new_path

    return None

def iterative_deepening(graph,start,goal):
    for depth in range(100):
        path = iddfs(graph,start,goal,depth)

        if path is not None:
            return path
    return None

def get_path_cost(graph,path):
    cost = 0
    for i in range(len(path)-1):
        cost += graph[path[i]][path[i+1]]
    return cost


def create_graph():
 # Creating a graph
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
path = iterative_deepening(graph,"zerind","bucharest")

if path:
    print("Path : ",path)
    print("Path cost : ",get_path_cost(graph,path))
else:
    print("No path found")