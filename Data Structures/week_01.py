import sys


def parentheses_match(user_input):
    check = []
    for i in range(0, len(user_input)):

        if user_input[i] == '{' or user_input[i] == '[' or user_input[i] == '(':
            check.append(user_input[i])

        if user_input[i] == '}' and check.pop() != '{':
            return i
        if user_input[i] == ']' and check.pop() != '[':
            return i
        if user_input[i] == ')' and check.pop() != '(':
            return i

    if len(check) == 0:
        print("Success")
    else:
        print(len(check))


def find_children(tree, node):
    return [i for i, x in enumerate(tree) if x == node]


def construct_tree(user_input):
    tree = {}
    for i in range(0, len(user_input)):
        tree[i] = find_children(user_input, i)

    return tree, user_input.index(-1)


def find_depth(user_input):
    tree, root = construct_tree(user_input)

    queue = [tree[root]]
    height = 1
    while len(queue) != 0:
        level = queue[0]
        height += 1
        for node in level:
            if len(tree[node]) != 0:
                queue.append(tree[node])

        del queue[0]

    print(height)


def process_input_packets(user_input):
    user_input = [line.strip('\n') for line in user_input]
    return [map(int, line.split()) for line in user_input]


def process_packets(user_input):
    packets = process_input_packets(user_input)
    if len(packets) == 1:
        return packets[0][1]

    start_time = 0
    for i in range(0, len(packets)):
        if i == 0:
            packets[i].append(start_time+packets[i][1])
            start_time = packets[i][2]

        elif packets[i-1][0] == packets[i][0]:
            return -1

        else:
            packets[i].append(start_time+packets[i][1])

    return packets[-2][2]


def main():
    user_input = sys.stdin.readline()
    parentheses_match(list(user_input))

    user_input = sys.stdin.readline()
    user_input = map(int, user_input.split())
    find_depth(user_input)

    user_input = sys.stdin.readlines()
    print(process_packets(user_input))

if __name__ == "__main__":
    main()
