import sys

"""
For almost complete binary tree
"""


def process_input(user_input):
    user_input = [line.strip('\n') for line in user_input]
    user_input = [map(int, line.split()) for line in user_input]
    return user_input[0][0], user_input[1:]


def build_binary_tree(tree, array, i, root):
    tree[root] = array[i][0]
    print(root, array[i], tree)

    if array[i][1] != -1:
        build_binary_tree(tree, array, array[i][1], root * 2 + 1)

    if array[i][2] != -1:
        build_binary_tree(tree, array, array[i][2], root * 2 + 2)

    return tree


def is_binary(tree, root):
    if ((root*2)+1) < len(tree) and tree[root] > tree[(root*2)+1]:
        is_binary(tree, (root*2)+1)
    else:
        return -1

    if ((root*2)+2) < len(tree) and tree[root] < tree[(root*2)+2]:
        is_binary(tree, (root*2)+2)
    else:
        return -1

    return 0


def binary_tree(user_input):
    nodes, array = process_input(user_input)
    tree = [0] * nodes
    print(build_binary_tree(tree, array, 0, 0))
    print(is_binary(tree, 0))


def main():
    user_input = sys.stdin.readlines()
    binary_tree(user_input)

if __name__ == "__main__":
    main()