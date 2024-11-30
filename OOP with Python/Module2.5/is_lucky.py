


def is_lucky(number):
    while number > 0:
        digit = number % 10
        if digit != 4 and digit != 7:
            return False
        number //= 10
    return True

def find_lucky_numbers(A, B):
    lucky_numbers = []
    for num in range(A, B + 1):
        if is_lucky(num):
            lucky_numbers.append(num)

    if lucky_numbers:
        print(" ".join(map(str, lucky_numbers)))
    else:
        print(-1)

A, B = map(int, input().split())
find_lucky_numbers(A, B)