

# James Morrissey
# computingID: jpm9rk
# Checks if entered credit card number is valid

def check(credit_number):
    """
    Determines if a given credit card number is valid or not.

    :param(int) credit_number: credit card number whose validity is to be checked
    :return: True if the credit card number is valid, False if it is not
    """
    sum_every_other = 0
    sum_double_remain = 0
    remaining_num_string = ''
    remaining_num = []
    credit_number_list = list(str(credit_number))
    for i in range(0,len(credit_number_list)):
        if len(credit_number_list) % 2 == 0:
            if (i == 0) or (i % 2 == 0 and i>1):
                remaining_num.append(2*int(credit_number_list[i]))
            else:
                sum_every_other += int(credit_number_list[i])
        elif len(credit_number_list) == 1:
            remaining_num.append(credit_number_list[0])
        else:
            if i % 2 == 0:
                sum_every_other += int(credit_number_list[i])
            else:
                remaining_num.append(2*int(credit_number_list[i]))
    for k in range(len(remaining_num)):
        remaining_num_string+= str(remaining_num[k])
    remaining_digits = list(remaining_num_string)
    for j in range(len(remaining_digits)):
        sum_double_remain += int(remaining_digits[j])
    if (sum_every_other + sum_double_remain) % 10 == 0:
        return True
    else:
        return False


