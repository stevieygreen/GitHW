# Even first

def even_odd(arr):
    even = [] # creating a list where all the even numbers can be stored
    odd = [] # creating a list where all the odd numbers can be stored
    for num in num_list:
        if num % 2 == 0: # if a number is divided by 2 and theres no remainder (0) then it is even
            even.append(num) # take the even list and add this even number to it
        else:
            odd.append(num) # if it aint then it must be odd so add it to the odd list
        even.sort() # to put in order
        odd.sort() # to put in order
    return even + odd #combined both list


num_list = [3, 6, 4, 7, 9, 12, 15, 22]

results = even_odd(num_list)
print(results)