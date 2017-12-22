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

    if array[i][1] != -1:
        build_binary_tree(tree, array, array[i][1], root * 2 + 1)

    if array[i][2] != -1:
        build_binary_tree(tree, array, array[i][2], root * 2 + 2)

    return tree


def inorder_traversal(tree, root, traversal=[]):

    if ((root*2)+1) < len(tree):
        inorder_traversal(tree, (root*2)+1)

    traversal.append(tree[root])

    if ((root*2)+2) < len(tree):
        inorder_traversal(tree, (root*2)+2)

    return traversal


def preorder_traversal(tree, root, traversal=[]):

    traversal.append(tree[root])

    if ((root*2)+1) < len(tree):
        preorder_traversal(tree, (root*2)+1)

    if ((root*2)+2) < len(tree):
        preorder_traversal(tree, (root*2)+2)

    return traversal


def postorder_traversal(tree, root, traversal=[]):
    if ((root*2)+1) < len(tree):
        postorder_traversal(tree, (root*2)+1)

    if ((root*2)+2) < len(tree):
        postorder_traversal(tree, (root*2)+2)

    traversal.append(tree[root])

    return traversal


def is_binary(tree, root):
    if ((root*2)+1) < len(tree) and tree[root] > tree[(root*2)+1]:
        is_binary(tree, (root*2)+1)
    else:
        return False

    if ((root*2)+2) < len(tree) and tree[root] < tree[(root*2)+2]:
        is_binary(tree, (root*2)+2)
    else:
        return False

    return True


def main():
    user_input = sys.stdin.readlines()
    nodes, array = process_input(user_input)
    tree = [0] * nodes
    tree = build_binary_tree(tree, array, 0, 0)
    if is_binary(tree, 0):
        print("Is binary search tree")
    else:
        print("Is not binary search tree")

    print("Inorder Traversal", inorder_traversal(tree, 0))
    print("Preorder Traversal", preorder_traversal(tree, 0))
    print("Postorder Traversal", postorder_traversal(tree, 0))

if __name__ == "__main__":
    main()