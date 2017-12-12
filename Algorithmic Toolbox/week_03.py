def changing_money(value, coins):
    print value, coins, "else",
    if value <= 0:
        return coins

    else:
        value_in_bag = coins[0] + 5 * coins[1] + 10 * coins[2]
        print value_in_bag, coins

        if value - value_in_bag > 10:
            units = value / 10
            value -= units * 10
            coins[2] += units
        elif value - value_in_bag > 5:
            units = value / 5
            value -= units * 5
            coins[1] += units
        else:
            units = value
            value -= units
            coins[0] += units

        changing_money(value, coins)


def main():
    coins = [0, 0, 0]
    value = int(raw_input())
    coins = changing_money(value, coins)
    print coins


if __name__ == "__main__":
    main()