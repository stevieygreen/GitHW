# Find Two Lowest Elements In a List


def find_tow_lowest_numbers_in_list(number_list):
    number_list.sort()
    return number_list[:2]


number_list = [3, 1, 1, 4, 5, 6, 5]

result = find_tow_lowest_numbers_in_list(number_list)
print(result)
