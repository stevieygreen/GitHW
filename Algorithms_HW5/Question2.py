# Bubble sort descending order

def bubble_sort_descending(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place, so we only need to compare the first n-i elements
        for j in range(0, n - i - 1):
            # Swap adjacent elements if they are in the wrong order
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


test_list2 = [3, 9, 2, 6, 7, 3, 37, 28]
result = bubble_sort_descending(test_list2)
print(result)