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

my_graph = {
    'A': [('B', 3), ('D', 1)],
    'B': [('A', 3), ('C', 4)],
    'C': [('B', 4), ('D', 7)],
    'D': [('A', 1), ('C', 7)]
}

def shortest_path(graph, start):
    unvisited = []
    distances = {}
    for node in graph:
        unvisited.append(node)
        if node == start:
            distances[node] = 0
        else:
            distances[node] = float('inf')
    print(f'Unvisited: {unvisited}\nDistances: {distances}')
    
shortest_path(my_graph, 'A')