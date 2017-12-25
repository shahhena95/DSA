import sys


def rotate_and_sort(text):
    text = text[-1] + text[:len(text)-1]
    rotations = []

    for i in range(0, len(text)):
        before = text[:len(text) - 1]
        after = text[len(text) - 1:]
        text = before[::-1] + after[::-1]
        text = text[::-1]
        rotations.append(text)

    return sorted(rotations)


def bwt(text):
    sorted_rotations = rotate_and_sort(text)
    last_col = [row[-1] for row in sorted_rotations]
    print("".join(last_col))


def main():
    user_input = sys.stdin.readline().strip('\n')
    bwt(user_input)


if __name__ == "__main__":
    main()