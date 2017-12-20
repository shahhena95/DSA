import sys


#get into a better format. Ask Emilien
def process_input_dijakstra(user_input):
    user_input = [map(int, line.split()) for line in user_input]

    vertices = user_input[0][0]
    graph = {}
    for i in range(1, vertices+1):
        graph[i] = []

    for i in range(1, len(user_input)-1):
        graph[user_input[i][0]].append([user_input[i][1], user_input[i][2]])

    return graph, vertices, user_input[-1][0], user_input[-1][1]


def process_input_bellman(user_input):
    user_input = [map(int, line.split()) for line in user_input]

    vertices = user_input[0][0]
    graph = {}
    for i in range(1, vertices+1):
        graph[i] = []

    for i in range(1, len(user_input)):
        graph[user_input[i][0]].append([user_input[i][1], user_input[i][2]])

    return graph, vertices+1


def min_distance(vertices, distance, visited):
    min_dist, min_index = sys.maxint, -1
    for v in range(1, vertices):
        if distance[v] < min_dist and not visited[v]:
            min_dist = distance[v]
            min_index = v
    if min_index == -1:
        return (visited[1:].index(False))+1

    return min_index


def get_edge(graph, u, v):
    for child in graph[u]:
        if child[0] == v:
            return child[1]
    return sys.maxint


def get_output_format(distance):
    for i in range(len(distance)):
        if distance[i] == sys.maxint:
            distance[i] = -1

    return distance


def shortest_path_dijakstra(user_input):
    graph, vertices, start, end = process_input_dijakstra(user_input)
    adjust_index = vertices + 1

    visited, distance = [False]*adjust_index, [sys.maxint]*adjust_index
    distance[start] = 0

    for iterations in range(vertices):
        u = min_distance(adjust_index, distance, visited)

        visited[u] = True
        for v in range(1, adjust_index):
            edge = get_edge(graph, u, v)

            if edge > 0 and not visited[v] and distance[v] > distance[u] + edge:
                distance[v] = distance[u] + edge

    distance = get_output_format(distance)

    return distance[end]


def detect_negative_cycle(graph, distance, vertices):
    for u in range(1, vertices):
        for v in range(1, vertices):
            edge = get_edge(graph, u, v)

            if distance[v] > distance[u] + edge:
                return -1
    return 0


def bellman_ford(user_input):
    graph, vertices = process_input_bellman(user_input)

    distance = [sys.maxint]*vertices
    distance[1] = 0

    for u in range(1, vertices):
        for v in range(1, vertices):
            edge = get_edge(graph, u, v)
            if distance[v] > distance[u] + edge:
                distance[v] = distance[u] + edge

    return detect_negative_cycle(graph, distance, vertices)


def main():
    user_input = sys.stdin.readlines()
    user_input = [line.strip('\n') for line in user_input]
    print(shortest_path_dijakstra(user_input))
    print(bellman_ford(user_input))


if __name__ == "__main__":
    main()
