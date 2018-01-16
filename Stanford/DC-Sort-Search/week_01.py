def get_digits(number):
    return len(str(number))-1


def karatsuba(x, y, n):

    a = x / (10 ** n)
    b = x % (10 ** n)
    c = y / (10 ** n)
    d = y % (10 ** n)
    if n < 1:
        return x * y
    else:
        z1 = karatsuba(a, c, min(get_digits(a), get_digits(c)))
        z2 = karatsuba(a, d, min(get_digits(a), get_digits(d)))
        z3 = karatsuba(b, c, min(get_digits(b), get_digits(c)))
        z4 = karatsuba(b, d, min(get_digits(b), get_digits(d)))

        return (10 ** n) * z1 + (10 ** (n//2)) * (z2 + z3) + z4


number_1 = 3141592653589793238462643383279502884197169399375105820974944592
number_2 = 2718281828459045235360287471352662497757247093699959574966967627
print karatsuba(number_1, number_2, min(get_digits(number_1), get_digits(number_2)))
