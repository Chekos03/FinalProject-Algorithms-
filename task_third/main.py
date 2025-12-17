import matplotlib.pyplot as plt
import networkx as nx
import heapq

G = nx.Graph()

red_line = ["Академмістечко", "Святошин" , "Берестейська" , "Шулявська" , "Вокзальна" , "Університет" , "Театральна", "Хрещатик"]
blue_line = ["Героїв Дніпра" , "Оболонь" , "Почайна" , "Контрактова площа" , "Поштова площа" , "Майдан Незалежності" , "Площа Українських Героїв"]
green_line = ["Сирець" , "Дорогожичі" , "Лук'янівська" , "Золоті ворота" , "Палац спорту" , 'Кловська']
red_weights = [3, 4, 3, 2, 3, 2,2]
blue_weights = [4, 3, 2, 3, 2, 3]
green_weights = [3, 4, 2, 3, 3]
transfer_weight = 1 

def creating_edges(line, weights):
    for i in range(len(line)-1):
        G.add_edge(line[i], line[i+1], weight=weights[i])

creating_edges(red_line, red_weights)
creating_edges(blue_line, blue_weights)
creating_edges(green_line, green_weights)


transfers = [("Театральна", "Золоті ворота"),
            ("Хрещатик", "Майдан Незалежності"),
            ("Палац спорту", "Площа Українських Героїв")]

for a, b in transfers:
    G.add_edge(a, b, weight=transfer_weight)


pos = nx.spring_layout(G, seed=7) 
nx.draw(G, pos, with_labels=True, node_size=1500, font_size=9)
plt.show()



def dijkstra(graph, start):
    dist = {vertex: float('inf') for vertex in graph.nodes}
    dist[start] = 0
    visited = set()
    heap = [(0, start)]

    while heap:
        current_dist, current_vertex = heapq.heappop(heap)
        if current_vertex in visited:
            continue
        visited.add(current_vertex)

        for neighbor, attrs in graph[current_vertex].items():
            weight = attrs['weight']
            new_dist = current_dist + weight

            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
    return dist




result = dijkstra(G, "Сирець")

for vertex, distance in result.items():
    print(f"Відстань від заданої точки до {vertex}: {distance}")