# Selection sort descending order

def selection_sort_descending(arr):
    n = len(arr)
    for i in range(n):
        # Find the maximum element in the unsorted portion of the array
        max_index = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:
                max_index = j

        # Swap the maximum element with the first element of the unsorted portion of the array
        arr[i], arr[max_index] = arr[max_index], arr[i]

    return arr


test_list = [0, 9, 2, 6, 7, 3, 37, 28]

result = selection_sort_descending(test_list)
print(result)