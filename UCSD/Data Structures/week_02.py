import sys


def build_heap(array):
    nodes = len(array)
    for i in range(nodes//2, -1, -1):
        heapify(array, i)
    return array


def heapify(array, i):
    left, right = 2 * i + 1, 2 * i + 2
    if left < len(array) and array[i] > array[left]:
        min_index = left
    else:
        min_index = i

    if right < len(array) and array[right] < array[min_index]:
        min_index = right

    if min_index != i:
        print(i, min_index)
        array[i], array[min_index] = array[min_index], array[i]
        heapify(array, min_index)

#TODO parallel processing Q2


def main():
    user_input = sys.stdin.readline()
    user_input = map(int, user_input.split())
    print(build_heap(user_input))

if __name__ == "__main__":
    main()
