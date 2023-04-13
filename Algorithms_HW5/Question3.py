# Insertion sort descending order

def insertion_sort_descending(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are less than key, to one position ahead of their current position
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


test_list3 = [5, 9, 2, 6, 7, 2, 88, 28]
result = insertion_sort_descending(test_list3)
print(result)