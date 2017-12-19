import sys


def process_input(user_input):
    """Input graph is directed"""
    user_input = [map(int, line.split()) for line in user_input]

    vertices = user_input[0][0]
    graph = {}
    for i in range(1, vertices+1):
        graph[i] = []

    for i in range(1, len(user_input)):
        graph[user_input[i][0]].append(user_input[i][1])

    return graph


def dfs_for_cycle(graph, root, visited=[], is_being_visited=[]):
    if root in is_being_visited:
        print("cycle at node", root)
        return False

    elif root in visited:
        return True

    else:
        visited.append(root)
        is_being_visited.append(root)
        for child in graph[root]:
            if not dfs_for_cycle(graph, child, visited, is_being_visited):
                return False
        is_being_visited.remove(root)
        return True


def detect_cycle(user_input):
    graph = process_input(user_input)
    if dfs_for_cycle(graph, 1):
        print(0)
    else:
        print(1)


def dfs_for_topsort(graph, root, visited=[], ordering=[]):
    visited.append(root)
    for child in graph[root]:
        if child not in visited:
            dfs_for_topsort(graph, child, visited, ordering)

    ordering.append(root)

    return visited, ordering


def top_sort(user_input):
    graph = process_input(user_input)
    visited, ordering = [], []
    for node in graph.keys():
        if node not in visited:
            visited, ordering = dfs_for_topsort(graph, node, visited)

    print(ordering[::-1])


def main():
    user_input = sys.stdin.readlines()
    user_input = [line.strip('\n') for line in user_input]
    # print(detect_cycle(user_input))
    print(top_sort(user_input))

if __name__ == "__main__":
    main()
