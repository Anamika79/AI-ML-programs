from collections import deque

def breadth_first_search(graph,start,goal):
    queue = deque([(start,[start])])

    while queue:
        vertex,path = queue.popleft()
        for neighbor in graph[vertex].keys():
            if neighbor == goal:
                return path + [neighbor]
            else:
                queue.append((neighbor,path+[neighbor]))

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
path = breadth_first_search(graph,"zerind","bucharest")

print("Path : ",path)
print("Path cost : ",get_path_cost(graph,path))
