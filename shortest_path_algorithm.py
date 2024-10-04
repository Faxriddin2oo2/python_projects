# Bismillah
"""
Created on Tue Oct  1 21:22:35 2024

@author: Faxriddin

Project : Building a Shortest Path Algorithm
"""



# copper = {
#     'species': 'guinea pig',
#     'age': 2
# }
# copper['food'] = 'hay'
# copper['species'] = 'Cavia porcellus'
# del copper['age']

# for i, j in copper.items():
#     print(i, j)

# my_graph = {
#     'A': [('B', 3), ('D', 1)],
#     'B': [('A', 3), ('C', 4)],
#     'C': [('B', 4), ('D', 7)],
#     'D': [('A', 1), ('C', 7)]
# }

# def shortest_path(graph, start):
#     unvisited = []
#     distances = {}
#     for node in graph:
#         unvisited.append(node)
#         if node == start:
#             distances[node] = 0
#         else:
#             distances[node] = float('inf')
#     print(f'Unvisited: {unvisited}\nDistances: {distances}')
    
# shortest_path(my_graph, 'A')



# The final result
my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C',1 ), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

def shortest_path(graph, start, target = ''):
    unvisited = list(graph)
    distances = {node: 0 if node == start else float('inf') for node in graph}
    paths = {node: [] for node in graph}
    paths[start].append(start)
    
    while unvisited:
        current = min(unvisited, key=distances.get)
        for node, distance in graph[current]:
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)
        unvisited.remove(current)
    
    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            continue
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
    
    return distances, paths
    
shortest_path(my_graph, 'A', 'F')