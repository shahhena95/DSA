import sys


"""
Phone book problem
is this feasible if numbers >= 10 ** 5 ?
"""


def process_input(user_input):
    user_input = [line.strip('\n') for line in user_input]
    user_input = [line.split(' ') for line in user_input]
    return user_input


def phone_book(user_input):
    user_input = process_input(user_input)
    contacts = {}
    for query in user_input:
        if query[0] == 'add':
            contacts = add_number(contacts, query[1], query[2])
        if query[0] == 'del':
            contacts = del_number(contacts, query[1])
        if query[0] == 'find':
            find_number(contacts, query[1])


def add_number(contacts, number, name):
    contacts[int(number)] = name
    return contacts


def del_number(contacts, number):
    if int(number) in contacts:
        del contacts[int(number)]

    return contacts


def find_number(contacts, number):
    if int(number) not in contacts:
        print("Not found")
    else:
        print(contacts[int(number)])


def main():
    user_input = sys.stdin.readlines()
    phone_book(user_input)

if __name__ == "__main__":
    main()
