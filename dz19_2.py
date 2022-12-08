import networkx as nx

def from_file_to_list(file_name: str):
    edge_cities = []
    with open("cities.csv") as file:
        for element in file:
            city_1, city_2, distance = element.split(';')
            edge_cities.append([city_1, city_2, distance])
    return edge_cities

edge_city_list = from_file_to_list("cities.csv")

print(edge_city_list)

graph = nx.Graph()

for edge in edge_city_list:
    graph.add_edge(edge[0], edge[1], weight = int(edge[2]))

def get_route(G, start_point, end_point):
    route = nx.shortest_path(G, start_point, end_point, weight="weight")
    dist = nx.shortest_path_length(G, start_point, end_point, weight="weight")
    return route, dist


edge_cities_list = from_file_to_list("cities.csv")
print(edge_cities_list)
graph = nx.Graph()

for edge in edge_cities_list:
    graph.add_edge(edge[0], edge[1], weight=int(edge[2]))

my_route, dist = get_route(graph, "Kyiv", "Lviv")
my_route1, dist1 = get_route(graph, "Lviv", "Kyiv")

print("-------------------\nMy route:", *my_route, sep=' - ')
print("-------------------\nTotal Distance = ", dist, "km")
print("-------------------\nMy route:", *my_route1, sep=' - ')
print("-------------------\nTotal Distance = ", dist1, "km")