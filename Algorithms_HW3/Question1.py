# Below The Arithmetical Mean aka average

def list_avg(n):
    sum_of_list = sum(numbers_in_list) # add up all the numbers together
    amount_in_list = len(numbers_in_list) # count total numbers in list
    average = sum_of_list / amount_in_list # divides sum of list by numbers in list to get the average
    lessthan_or_equal = [] #setting up return list
    for num in numbers_in_list: # for every number in this list
        if num <= average: # only take the numbers less than or equal to the average
            lessthan_or_equal.append(num) #go through the lest and add aka append the numbers that meat the critria
    return lessthan_or_equal # return the list of numbers that made the cut


numbers_in_list = [1, 2, 3, 4, 5, 6, 8]

results = list_avg(numbers_in_list)

print(results)

