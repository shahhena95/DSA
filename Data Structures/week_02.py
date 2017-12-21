import sys


def build_heap(array):
    root = array.index(min(array))
    while array[root] > array[root * 2 + 1] or array[root] > array[root * 2 + 2]: #can break here
        heapify(array, root)
        root = root * 2 + 1
        if root > len(array):
            break


def heapify(array, root_index):
    root = array[root_index]
    for i in range(root, len(array)):
        if array[i] > array[2 * i + 1]:
            min_leaf = min(array[2 * i + 1], array[2 * i + 2])
        min_leaf_index = array.index(min_leaf)
        array[i], array[min_leaf_index] = min_leaf, array[i]
        print(i, 2 * i + 1)

        print(array)
        if array[i] > array[2 * i + 2]:
            array[i], array[2 * i + 2] = array[2 * i + 2], array[i]
            print(i, 2 * i + 2)
        print(array)


def main():
    user_input = sys.stdin.readline()
    user_input = map(int, user_input.split())
    build_heap(user_input)

if __name__ == "__main__":
    main()
