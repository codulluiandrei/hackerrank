def count_substring(string, sub_string):
    counter = 0
    for i in range(0, len(string)):
        counter = counter + string.count(sub_string, i, i + len(sub_string))
    return counter
    
