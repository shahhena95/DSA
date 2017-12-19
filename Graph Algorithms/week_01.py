import sys


def process_find_exit_input(user_input):
    """Input graph is undirected"""
    user_input = [map(int, line.split()) for line in user_input]

    vertices = user_input[0][0]
    graph = {}
    for i in range(1, vertices+1):
        graph[i] = []

    for i in range(1, len(user_input)-1):
        graph[user_input[i][1]].append(user_input[i][0])
        graph[user_input[i][0]].append(user_input[i][1])

    return graph, user_input[-1][0], user_input[-1][1]


def process_add_exit_input(user_input):
    user_input = [map(int, line.split()) for line in user_input]

    vertices = user_input[0][0]
    graph = {}
    for i in range(1, vertices+1):
        graph[i] = []

    for i in range(1, len(user_input)):
        graph[user_input[i][1]].append(user_input[i][0])
        graph[user_input[i][0]].append(user_input[i][1])

    return graph


def connected_components(graph, visited=set(), count=0):
    for node in graph.keys():
        if node not in visited:
            visited = dfs(graph, node, visited)
            count += 1

    return count


def dfs(graph, root, visited=None):
    if visited is None:
        visited = set()

    visited.add(root)

    for child in graph[root]:
        if child not in visited:
            dfs(graph, child, visited)
    return visited


def find_exit(user_input):
    graph, start, end = process_find_exit_input(user_input)
    visited = dfs(graph, start)
    if end in visited:
        print(1)
    else:
        print(0)


def add_exit(user_input):
    graph = process_add_exit_input(user_input)
    print(connected_components(graph, set()))


def main():
    user_input = sys.stdin.readlines()
    user_input = [line.strip('\n') for line in user_input]
    print("Exit Maze", find_exit(user_input))
    print("Connected Components", add_exit(user_input))

if __name__ == "__main__":
    main()
