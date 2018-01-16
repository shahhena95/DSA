with open('./integer_array.txt') as f:
    array = f.readlines()
array = [int(line.strip('\n')) for line in array]

#avoid global
#O(1) is better
#Understand the tradeoff between memory-speed

count = 0


def merge_count(left, right):
    global count
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if right[j] > left[i]:
            count += len(left) - i
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def count_inversions(array):
    if len(array) > 2:
        m = len(array)/2
    else:
        return array

    return merge_count(count_inversions(array[:m]), count_inversions(array[m:]))

count_inversions(array)
print count
