import networkx as nx
from matplotlib import pyplot as plt

def create_graph(sets): # To update the weights of the edge
    Id_points = range(len(coordinate_sets))
    Id_markers = []

    for i in range(len(coordinate_sets)):
        Id_markers.append(coordinate_sets[i][0])
    Id_markers = Id_markers[1:]

    Distance_points = []
    Distance = []
    for i in range(len(coordinate_sets)):
        for j in range(len(coordinate_sets)):
            if i < j :
                distance = ((coordinate_sets[j][1] - coordinate_sets[i][1])**2 + (coordinate_sets[j][2] - coordinate_sets[i][2])**2)**(1/2)
                Distance_points.append([Id_points[i], Id_points[j], distance])
                Distance.append(distance)

    Id_markers_normalization = []
    for i in range(len(Id_markers)):
        id_n = (Id_markers[i] - min(Id_markers))/(max(Id_markers) - min(Id_markers)) + 1
        Id_markers_normalization.append(id_n)

    Distance_points_normalization = []
    d_min = min(Distance)
    d_max = max(Distance)
    for i in range(len(Distance_points)):
        distance_n = (Distance_points[i][2] - d_min)/(d_max - d_min) + 1
        Distance_points_normalization.append([Distance_points[i][0], Distance_points[i][1], distance_n])
    # By using normalization, let the Id of marker and distance have the same scale.

    Weights = []
    for i in range(len(Distance_points_normalization)):
        weight = Distance_points_normalization[i][2]/Id_markers_normalization[Distance_points_normalization[i][1] - 1]
        Weights.append([Distance_points_normalization[i][0], Distance_points_normalization[i][1], weight])

    G = nx.Graph()
    G.add_nodes_from(Id_points)
    G.add_weighted_edges_from(Weights)

    return G


if __name__ == '__main__':
    coordinate_sets = [[0, 0, 0],
                       [8, 4, 5],
                       [10, 5, 6],
                       [21, 8, 2],
                       [9, 6, 6]]
    # We stored the coordinates as [Id of marker, x, y] this form.
    # And we set the original point as [0, 0, 0]
    graph = create_graph(coordinate_sets)

    path = nx.single_source_dijkstra_path(graph, 4)
    length = nx.single_source_dijkstra_path_length(graph, 4)

    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, alpha=0.5)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.show()

    p = nx.floyd_warshall(graph)
    print(p)

    G2 = nx.Graph()
    G2.add_nodes_from([0,1,2,3,4])
    G2.add_weighted_edges_from([(0,3,0.9840306522192983),
                               (3,1,0.7671910246264386),
                               (1,2,0.9146254633293417),
                               (2,4,0.9285714285714286)])

    pos = nx.random_layout(G2)
    nx.draw(G2, pos, with_labels=True, alpha=0.5)
    labels = nx.get_edge_attributes(G2, 'weight')
    nx.draw_networkx_edge_labels(G2, pos, edge_labels=labels)
    plt.show()



