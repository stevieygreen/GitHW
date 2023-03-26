                                        #Split in Half (run the code to see what its doing)
def split_in_half(s):
    length_of_string = len(s) #save length of string in a variable
    cut_string_half = length_of_string // 2
    add = 0
    if length_of_string % 2:   #to see if its even or odd
        add = 1
    left = s[:cut_string_half + add]
    right = s[cut_string_half + add:]
    return right + left

str1_even = "aaabbb"
str2_odd = "aaabbbb"

result_even = split_in_half(str1_even)
result_odd = split_in_half(str2_odd)

print(result_even)
print(result_odd)