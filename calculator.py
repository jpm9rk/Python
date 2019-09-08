# James Morrissey
# computingID: jpm9rk


def binop(a_string):
    some_string = a_string.strip()
    if some_string.find('+') != -1:
        location = some_string.find('+')
        first_string = some_string[0:location]
        second_string = some_string[(location + 1):len(some_string)]
        num_string_1 = int(first_string)
        num_string_2 = int(second_string)
        return num_string_1 + num_string_2
    elif some_string.find('*') != -1:
        location = some_string.find('*')
        first_string = some_string[0:location]
        second_string = some_string[(location + 1):len(some_string)]
        num_string_1 = int(first_string)
        num_string_2 = int(second_string)
        return num_string_1 * num_string_2
    elif some_string.find('/') != -1:
        location = some_string.find('/')
        first_string = some_string[0:location]
        second_string = some_string[(location + 1):len(some_string)]
        num_string_1 = int(first_string)
        num_string_2 = int(second_string)
        return num_string_1 / num_string_2
    elif some_string.find('-') != -1:
        location = some_string.find('-')
        first_string = some_string[0:location]
        second_string = some_string[(location + 1):len(some_string)]
        num_string_1 = int(first_string)
        num_string_2 = int(second_string)
        return num_string_1 - num_string_2








