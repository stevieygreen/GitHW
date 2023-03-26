                                        #Unqiue Characters in String
# "abc" has unique characters, "abb" does not

def uni_char(s):
    chars = set()

    for char in s:
        if char in chars:
            return False
        else:
            chars.add(char)

    return True

str1 = "abc"
str2 = "abb"

result = uni_char(str2)
print(result)