import sys


def process_input(user_input):
    """Input graph is undirected"""
    user_input = [map(int, line.split()) for line in user_input]

    vertices = user_input[0][0]
    graph = {}
    for i in range(1, vertices+1):
        graph[i] = []

    for i in range(1, len(user_input)):
        graph[user_input[i][0]].append(user_input[i][1])

    return graph, user_input[-1][0], user_input[-1][1]


def shortest_path(user_input):
    """ Understanding - Shortest path in an undirected graph is obtained using bfs """
    graph, start, end = process_input(user_input)
    queue, visited, distance = [start], [start], 0

    while len(queue) != 0:
        root = queue[0]
        for child in graph[root]:
            if child == end:
                return distance

            if child not in visited:
                queue.append(child)
                visited.append(child)
                distance += 1

        queue.remove(root)

    return -1


def is_bipartite(user_input):
    graph, _, _ = process_input(user_input)
    red, black = set(), set()
    red.add(1)

    for node in graph.keys():
        if node in red:
            for child in graph[node]:
                black.add(child)
        if node in black:
            for child in graph[node]:
                red.add(child)

    if len(red & black) != 0:
        return True
    else:
        return False


def main():
    user_input = sys.stdin.readlines()
    user_input = [line.strip('\n') for line in user_input]
    print(shortest_path(user_input))
    print(is_bipartite(user_input))


if __name__ == "__main__":
    main()
