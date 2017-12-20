import sys
import math


def get_distance(x, y):
    return math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)


def process_input(user_input):
    user_input = [map(int, line.split()) for line in user_input]
    return user_input[1:]


def get_all_edges(nodes):
    edges = []
    for i in range(0, len(nodes)):
        edges.append([sys.maxint]*len(nodes))

    for i in range(0, len(nodes)):
        for j in range(0, len(nodes)):
            edges[i][j] = get_distance(nodes[i], nodes[j])

    return edges


def get_min_distance(distance, visited, nodes):
    min_dist, min_index = sys.maxint, -1
    for i in range(0, len(nodes)):
        if not visited[i] and distance[i] < min_dist:
            min_dist = distance[i]
            min_index = i

    if min_index == -1:
        return visited.index(False)
    else:
        return min_index


def minimum_spanning_tree(user_input):
    nodes = process_input(user_input)
    edges = get_all_edges(nodes)
    visited, distance = [False] * len(nodes), [sys.maxint] * len(nodes)
    distance[0], required_edges = 0, set()

    while False in visited:
        i = get_min_distance(distance, visited, nodes)

        visited[i] = True

        for j in range(0, len(nodes)):
            if not visited[j] and distance[j] > edges[i][j]:
                distance[j] = edges[i][j]

    return sum(distance)

# TODO clustering problem


def main():
    user_input = sys.stdin.readlines()
    user_input = [line.strip('\n') for line in user_input]
    print(minimum_spanning_tree(user_input))

if __name__ == "__main__":
    main()
