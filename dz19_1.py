
import networkx as nx
import matplotlib.pyplot as plt

edge_cities = []
with open("cities.csv") as file:
    for element in file:
        city_1, city_2, distance = element.strip().split(";")
        distance = int(distance)
        edge_cities.append([city_1, city_2, distance])

print(edge_cities)

graph = nx.Graph()

for edge in edge_cities:
    graph.add_edge(edge[0], edge[1], weight = edge[2])

pos = nx.spring_layout(graph)
nx.draw_networkx(graph, pos)
plt.title("Ukrainian Cities Graph")
plt.show()
nx.draw_networkx(graph)