# Compute the sum of digits in all numbers from 1 to n

def sum_num(n):
    total = 0
    for i in range(1, n+1):
        total += i
    print (total)

sum_num(10)