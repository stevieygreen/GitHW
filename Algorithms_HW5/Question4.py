# Merge sort descending order

def merge_sort_descending(arr: list):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    return merge_arrays_descending(merge_sort_descending(arr[:middle]), merge_sort_descending(arr[middle:]))


def merge_arrays_descending(left_arr: list, right_arr: list):
    merged_list = []
    i = j = 0
    while i < len(left_arr) or j < len(right_arr):
        if i == len(left_arr):
            merged_list.append(right_arr[j])
            j += 1
        elif j == len(right_arr):
            merged_list.append(left_arr[i])
            i += 1
        elif left_arr[i] > right_arr[j]:
            merged_list.append(left_arr[i])
            i += 1
        else:
            merged_list.append(right_arr[j])
            j += 1
    return merged_list


test_list4 = [5, 9, 2, 6, 7, 2, 88, 28]
print(test_list4)
print(merge_sort_descending(test_list4))