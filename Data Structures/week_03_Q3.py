import sys


def create_hash(pattern):
    hpattern, power = 0, 0
    for letter in pattern:
        hpattern += ord(letter) * 256 ** power
        power += 1
    return hpattern


def recalculate_hash(htext, new_char, prev_char, n):
    htext -= ord(prev_char)
    htext /= 256
    htext += ord(new_char) * 256 ** (n-1)
    return htext


def rabin_karp(pattern, text):
    m, n = len(text), len(pattern)
    hpattern = create_hash(pattern)
    htext = create_hash(text[0:n])

    for i in range(0, m-n+1):

        if htext == hpattern:
            if text[i:i+n] == pattern:
                print(i)

        if i+n < m:
            htext = recalculate_hash(htext, text[i+n], text[i], n)


def main():
    user_input = sys.stdin.readlines()
    user_input = [line.strip('\n') for line in user_input]
    pattern, text = user_input[0], user_input[1]
    rabin_karp(pattern, text)


if __name__ == "__main__":
    main()