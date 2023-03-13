# Find the max number from 3 values

def find_max_number(a, b, c):
    if a >= b and a >= c:
        print(a)
    elif b >= a and b >= c:
        print(b)
    else:
        print(c)


find_max_number(9, 654, 200)
