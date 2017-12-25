import sys

"""
Hashing with chains problem
"""


def flatten(lst):
    return [item for sublist in lst for item in sublist]


def process_input(user_input):
    user_input = [line.strip('\n') for line in user_input]
    buckets = int(user_input[0][0])
    del user_input[0]
    user_input = [line.split(' ') for line in user_input]
    return buckets, user_input


def h(word, buckets, p=1000000007, x=263):
    hash_value = 0
    for i in range(len(word)):
        hash_value += (ord(word[i]) * (x ** i))

    return hash_value % p % buckets


def add(hash_map, word, buckets):
    values = flatten(hash_map.values())
    if word in values:
        return hash_map

    hash_key = h(word, buckets)
    if hash_key in hash_map:
        hash_map[hash_key].append(word)
    else:
        hash_map[hash_key] = []
        hash_map[hash_key].append(word)
    return hash_map


def delete(hash_map, word):
    for key, values in hash_map.items():
        if word in values:
            values.remove(word)
    return hash_map


def find(hash_map, word):
    values = flatten(hash_map.values())
    if word in values:
        print("yes")
    else:
        print("no")


def check(hash_map, hash_key):
    if hash_key in hash_map:
        print(hash_map[hash_key][::-1])


def hash_with_chains(user_input):
    buckets, user_input = process_input(user_input)
    hash_map = {}
    for query in user_input:
        if query[0] == 'add':
            hash_map = add(hash_map, query[1], buckets)
        if query[0] == 'del':
            hash_map = delete(hash_map, query[1])
        if query[0] == 'find':
            find(hash_map, query[1])
        if query[0] == 'check':
            check(hash_map, int(query[1]))


def main():
    user_input = sys.stdin.readlines()
    hash_with_chains(user_input)

if __name__ == "__main__":
    main()
