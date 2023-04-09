# Increment a number
# takes a list turns it into one number, adds 1 then turns it to a list again

def manipulate_list(number_list):
    number_string = "".join(map(str, number_list)) #this turns the list of numbers into a string, but also combines the numbers to one instead of being seperate on a list its one string (map is used to transform)
    number_integer = int(number_string) #turns it back into a whole combined integer so we can add to it
    number_integer += 1 #add 1
    result = list(map(int, str(number_integer))) # creates a list, maps is used to transform
    return result


number_list = [1, 2, 9]
answer = manipulate_list(number_list)
print(answer)
