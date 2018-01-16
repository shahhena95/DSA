import sys


def get_edit_distance(string_a, string_b):
    n = len(string_a)
    m = len(string_b)
    distance = [[0 for _ in range(0, n)] for _ in range(0, m)]

    for i in range(0, n):
        for j in range(0, m):
            if i == 0:
                distance[i][j] = j

            elif j == 0:
                distance[i][j] = i

            elif string_a[i-1] == string_b[j-1]:
                distance[i][j] = distance[i-1][j-1]

            else:
                distance[i][j] = 1 + min(distance[i][j-1], distance[i-1][j], distance[i-1][j-1])
    print(distance)
    return distance[n-1][m-1]


def get_operation_result(operator, value_a, value_b):
    if operator == '+':
        return value_a + value_b

    if operator == '-':
        return value_a - value_b

    if operator == '*':
        return value_a * value_b


def get_min_max(operators, min_matrix, max_matrix, i, j):
    min_value, max_value = 100000000, -10000000
    for k in range(i, j):
        a = get_operation_result(operators[k], int(min_matrix[i][k]), int(min_matrix[k+1][j]))
        b = get_operation_result(operators[k], int(min_matrix[i][k]), int(max_matrix[k+1][j]))
        c = get_operation_result(operators[k], int(max_matrix[i][k]), int(min_matrix[k+1][j]))
        d = get_operation_result(operators[k], int(max_matrix[i][k]), int(max_matrix[k+1][j]))

        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)

    return min_value, max_value


def process_expression(user_input):
    digits, operators = [], []
    for i in range(0, len(user_input)):
        if user_input[i].isdigit():
            digits.append(int(user_input[i]))
        else:
            operators.append(user_input[i])

    return digits, operators


def get_max_min_expr(user_input):
    digits, operators = process_expression(user_input)

    min_matrix = [[0 for _ in range(0, len(digits))] for _ in range(0, len(digits))]
    max_matrix = [[0 for _ in range(0, len(digits))] for _ in range(0, len(digits))]

    for i in range(0, len(digits)):
            min_matrix[i][i], max_matrix[i][i] = digits[i], digits[i]

    for s in range(1, len(digits)):
        for i in range(0, len(digits)-s):
            j = i + s
            min_matrix[i][j], max_matrix[i][j] = get_min_max(operators, min_matrix, max_matrix, i, j)

    print("Minimum Value", min_matrix[0][len(digits)-1])
    print("Maximum Value", max_matrix[0][len(digits)-1])


def primitive_calc(user_input):
    if user_input == 1:
        return 0

    min_operations = [0 for _ in range(0, user_input+1)]
    min_operations[1], min_operations[2], min_operations[3] = 0, 0, 0

    for i in range(2, user_input+1):
        operations_1, operations_2, operations_3 = 1000000, 1000000, 1000000

        if (i/3) * 3 == i:
            operations_3 = min_operations[i/3]

        if (i/2) * 2 == i:
            operations_2 = min_operations[i/2]

        operations_1 = min_operations[i-1]

        min_operations[i] = 1 + min(operations_3, operations_2, operations_1)

    return min_operations[-1]


def main():

    user_input = sys.stdin.readlines()
    user_input = [line.strip('\n') for line in user_input]
    print(get_edit_distance(user_input[0], user_input[1]))

    user_input = sys.stdin.readline()
    user_input = user_input.split()
    get_max_min_expr(user_input)

    user_input = int(sys.stdin.readline())
    print(primitive_calc(user_input))

if __name__ == "__main__":
    main()
