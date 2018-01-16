# Time Constraints: 5 sec
# Constraints: n <= 45
fibonacci_series = {0: 0, 1: 1}


def fibonacci(number):
    if number in fibonacci_series:
        return fibonacci_series[number]
    else:
        fibonacci_series[number] = fibonacci(number-1) + fibonacci(number-2)
        return fibonacci_series[number]


# Constraints: n <= 10**7
def fibonacci_last_digit(value):
    fibonacci_last_digit_series = [0] * (value+1)
    fibonacci_last_digit_series[1] = 1

    for i in range(2, value+1):
        fibonacci_last_digit_series[i] = (fibonacci_last_digit_series[i-1] + fibonacci_last_digit_series[i-2]) % 10

    return fibonacci_last_digit_series[value]


# Constraints: 1 <= a, b <= 2. 10^9
def gcd(a, b):
    if a == 0:
        return b

    return gcd(b % a, a)


# Constraints: 1 <= a, b <= 2. 10^9
def lcm(a, b):
    return (a * b) / gcd(a, b)


# Constraints: n <= 10^18, m <= 10^5
def fibonacci_huge(n, m):
    period = n+1
    length_period = min(n+1, m*m+1)

    fibonacci_huge_series = [0] * length_period
    fibonacci_huge_series[0] = 0
    fibonacci_huge_series[1] = 1
    fibonacci_huge_series[2] = 1

    for i in range(3, length_period):
        fibonacci_huge_series[i] = (fibonacci_huge_series[i-1] + fibonacci_huge_series[i-2]) % m
        if fibonacci_huge_series[i] == 1 and fibonacci_huge_series[i-1] == 0:
            period = i-1
            break

    index = n % period
    return fibonacci_huge_series[index]


#TODO sum_fibonacci using pisano period series


# Constraints: 0 <= m <= n <= 10**18
def fibonacci_last_digit_partial_sum(m, n):  #Slow for higher input values
    fibonacci_partial_sum = [0] * (n+1)
    fibonacci_partial_sum[1] = 0
    fibonacci_partial_sum[2] = 1

    for i in range(3, n+1):
        fibonacci_partial_sum[i] = fibonacci_partial_sum[i-1] + fibonacci_partial_sum[i-2]

    return (sum(fibonacci_partial_sum[m:n])) % 10


def main():
    n = int(raw_input("For Fibonacci value (<= 45)"))
    print fibonacci(n)

    n = int(raw_input("For Fibonacci Last Digit value ( <= 10^7)"))
    print fibonacci_last_digit(n)

    value = map(int, (raw_input("For GCD and LCM (<= 10^9)")).split())
    print "GCD", gcd(value[0], value[1])
    print "LCM", lcm(value[0], value[1])

    value = map(int, (raw_input("For huge fibonacci modulo (<= 10^18, <= 10^5)")).split())
    print fibonacci_huge(value[0], value[1])

    value = map(int, (raw_input("For huge fibonacci partial last digit sum (0 <= m <= n <= 10**18)")).split())
    print fibonacci_last_digit_partial_sum(value[0], value[1])


if __name__ == "__main__":
    main()