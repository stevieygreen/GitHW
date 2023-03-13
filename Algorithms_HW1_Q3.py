# Count odd and even digits of the whole number

def count_digits(num):

    odd = 0
    even = 0

    for digit in str(num):
        if int(digit) % 2 == 0:
            even += 1
        else:
            odd += 1

    print(f"Even: {even}")
    print(f"Odd: {odd}")


count_digits(125576)