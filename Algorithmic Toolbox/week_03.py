from __future__ import division
import sys


def knapsack_money_change(value, coins):
    if value == 0:
        return coins

    else:
        if value >= 10:
            units = value / 10
            value -= (units*10)
            coins[2] += units

        elif value >= 5:
            units = value / 5
            value -= (units*5)
            coins[1] += units

        else:
            units = value
            value -= units
            coins[0] += units

        return knapsack_money_change(value, coins)


def process_max_loot_input(user_input):
    user_input = [map(int, line.split()) for line in user_input]

    n, weight = user_input[0][0], user_input[0][1]
    weights_per_value = {}
    for i in range(1, n+1):
        weight_i = user_input[i][0] / user_input[i][1]
        weights_per_value[weight_i] = [user_input[i][0], user_input[i][1]]

    return weight, weights_per_value


def get_max_weights(weights_per_value):
    """
    :param weights_per_value:
    :return: Tuple with maximum weight and maximum weight per value
    """
    key_list = weights_per_value.keys().sort()
    max_weight_per_value = key_list[-1]
    max_weight = weights_per_value[max_weight_per_value][0]
    return max_weight_per_value, max_weight


# Constraints : 1 <= n <= 10**3, 0 <= W, w <= 2. 10**6, 0 <= v <= 2. 10**6
def get_maximum_loot(input_value):
    weight, weights_per_value = process_max_loot_input(input_value)
    max_loot = 0

    while weight > 0:
        if weights_per_value == {}:
            return "Weights Insufficient"

        else:
            max_weight_per_value, max_weight = get_max_weights(weights_per_value)

            if weight > max_weight:
                max_loot += max_weight
            else:
                max_loot += weight * max_weight_per_value

            weight -= weights_per_value[max_weight_per_value][1]
            weights_per_value.pop(max_weight_per_value)

    return format(max_loot, '.4f')


def process_ad_input(user_input):
    return map(int, user_input[1].split()), map(int, user_input[2].split())


# Constraints : length of list <= 10**3, 0 <= a, b <= 10**5
def get_max_ad_revenue(user_input):
    profit_per_click, daily_avg_clicks = process_ad_input(user_input)

    profit_per_click.sort()
    daily_avg_clicks.sort()

    return sum([profit * clicks for profit, clicks in zip(profit_per_click, daily_avg_clicks)])


def process_visit_count_input(user_input):
    user_input = [tuple(map(int, line.split())) for line in user_input]
    del user_input[0]
    return user_input


def sort_min_right(segments):
    segments = sorted(segments, key=lambda x: x[1])
    return segments


def get_visit_count(user_input):
    segments = process_visit_count_input(user_input)
    segments = sort_min_right(segments)
    points = []
    i, j = 0, 0

    while i < len(segments):
        position = segments[i][1]
        points.append(position)
        i += 1
        while i < len(segments) and segments[i][0] <= position <= segments[i][1]:
            i += 1

    print(points)


def get_max_prize_places(user_input, pairwise_integers, count):
    if user_input - count > pairwise_integers[-1] + 1:
        pairwise_integers.append(count)
        user_input -= count
        count += 1
        get_max_prize_places(user_input, pairwise_integers, count)

    else:
        pairwise_integers.append(user_input)
        print(pairwise_integers[1:])


def get_max_digit(user_input):
    single_digits = []
    numbers = []
    result = ""
    for digit in user_input:
        if len(digit) == 1:
            single_digits.append(digit)
        else:
            numbers.append(digit)

    single_digits.sort()
    numbers.sort()

    while len(single_digits) > 0 and len(numbers) > 0:
        max_single = single_digits[-1]
        max_other = numbers[-1][0]

        if max_single >= max_other:
            result += max_single
            del single_digits[-1]
        else:
            result += numbers[-1]
            del numbers[-1]

    if len(single_digits) == 0:
        for digit in numbers:
            result += digit
    else:
        for digit in single_digits:
            result += digit

    print(result)


def main():
    # coins = [0, 0, 0]
    # value = int(input())
    # coins = knapsack_money_change(value, coins)
    # print(coins)
    #
    # user_input = sys.stdin.readlines()
    # user_input = [line.strip('\n') for line in user_input]
    # print(get_maximum_loot(user_input))
    #
    # user_input = sys.stdin.readlines()
    # user_input = [line.strip('\n') for line in user_input]
    # print(get_max_ad_revenue(user_input))
    #
    user_input = sys.stdin.readlines()
    user_input = [line.strip('\n') for line in user_input]
    print(get_visit_count(user_input))
    #
    # user_input = int(input())
    # get_max_prize_places(user_input, [0], 1)
    #
    # user_input = raw_input()
    # user_input = user_input.split()
    # get_max_digit(user_input)

if __name__ == "__main__":
    main()
