import sys
import random


def process_binary_search_input(user_input):
    return map(int, user_input[0].split()), map(int, user_input[1].split())


# Iteration Better Than Recursion
def binary_search(series, element, start, end):
    if element > series[-1] or element < series[0]:
        print(-1)
        return

    mid_index = start + ((end - start) / 2)
    if series[mid_index] == element:
        print(mid_index)
        return mid_index

    if series[mid_index] > element:
        binary_search(series, element, start, mid_index)

    else:
        binary_search(series, element, mid_index, end)


def get_count(series, element):
    return series.count(element)


def get_majority_element(series, left, right):
    if right - left == 1:
        return series[left]

    mid = left + (right-left) / 2

    majority_left = get_majority_element(series, left, mid)
    majority_right = get_majority_element(series, mid, right)

    if get_count(series, majority_left) >= get_count(series, majority_right):
        return majority_left
    elif get_count(series, majority_left) <= get_count(series, majority_right):
        return majority_right
    else:
        return -1


def partition3(series, left, right):
    pivot = series[right]
    m1, m2 = left-1, right
    for j in range(left, right+1):
        if series[j] < pivot:
            m1 += 1
            series[m1], series[j] = series[j], series[m1]

        elif series[j] > pivot:
            series[m2], series[j] = series[j], series[m2]
            m2 -= 1

    series[m1 + 1], series[right] = series[right], series[m1 + 1]
    return m1, m2


def partition2(series, left, right):
    pivot = series[right]
    i, j = left-1, left
    while j <= right:
        if series[j] < pivot:
            i += 1
            series[i], series[j] = series[j], series[i]
        j += 1

    series[i+1], series[right] = series[right], series[i+1]
    return i+1


def quick_sort(series, left, right):
    if left >= right:
        return

    k = random.randint(left, right)
    series[k], series[right] = series[right], series[k]
    # m = partition2(series, left, right)
    # quick_sort(series, left, m-1)
    # quick_sort(series, m+1, right)
    # print(left, k, right, series, m)
    m1, m2 = partition3(series, left, right)
    quick_sort(series, left, m1)
    quick_sort(series, m2, right)
    return series


def main():
    user_input = sys.stdin.readlines()
    user_input = [line.strip('\n') for line in user_input]
    series, elements = process_binary_search_input(user_input)
    for element in elements:
        binary_search(series, element, 0, len(series)-1)

    user_input = sys.stdin.readline().split()
    user_input = map(int, user_input)
    print(get_majority_element(user_input, 0, len(user_input)-1))

    user_input = sys.stdin.readline().split()
    user_input = map(int, user_input)
    print(quick_sort(user_input, 0, len(user_input)-1))


if __name__ == "__main__":
    main()
