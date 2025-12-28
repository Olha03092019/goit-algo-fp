import heapq

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edge("A", "B", weight=4)
G.add_edge("A", "C", weight=2)
G.add_edge("B", "C", weight=1)
G.add_edge("B", "D", weight=5)
G.add_edge("C", "D", weight=8)
G.add_edge("C", "E", weight=10)
G.add_edge("D", "E", weight=2)
G.add_edge("D", "F", weight=6)
G.add_edge("E", "F", weight=3)


# Реалізація алгоритму Дейкстри
def dijkstra(graph, start):
    shortest_paths = {vertex: float('infinity') for vertex in graph.nodes()}
    shortest_paths[start] = 0
    priority_queue = [(0, start)]
    visited = set()

    while priority_queue:
        # вилучаємо вершину з мінімальною відстанню
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        # перевіряємо сусідів
        for neighbor in graph.neighbors(current_vertex):
            # беремо вагу ребра
            edge_weight = graph[current_vertex][neighbor]['weight']

            # обчислюємо відстань через поточну вершину
            distance = current_distance + edge_weight

            # якщо ми знайшли коротший шлях, оновлюємо його
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                # додаємо до пріоритетної черги
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_paths

if __name__ == '__main__':
    # Використання алгоритму Дейкстри
    start_vertex = "A"
    shortest_paths = dijkstra(G, start_vertex)

    print(f"Shortest paths from vertex '{start_vertex}':")
    for vertex, distance in sorted(shortest_paths.items()):
        print(f"{start_vertex} -> {vertex}: {distance}")

    # Візуалізація графа
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_edges(G, pos, width=2)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")

    plt.axis("off")
    plt.show()
