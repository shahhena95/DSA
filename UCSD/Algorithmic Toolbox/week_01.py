def max_pairwise_product(input_list):
    input_list = sorted(input_list)
    return input_list[-1]*input_list[-2]


def main():
    value = raw_input().split()
    value = map(int, value)
    print max_pairwise_product(value)


if __name__ == "__main__":
    main()