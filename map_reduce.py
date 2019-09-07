# James Morrissey
# computingID: jpm9rk

# map_function is a function that takes 2 arguments


def myreduce(my_function, my_list):
    """Repeatedly apply function to list and combine all elements into one value

    Arguments:
    my_function -- the function to be applied to list elements
    my_list -- the list to which the function is applied
    Returns:
    new_func_eval (float) -- the final function evaluation
    """
    my_list_copy = my_list.copy()
    old_func_eval = my_function(my_list_copy[0], my_list_copy[1])
    for i in range(2,len(my_list_copy)):
        new_func_eval = my_function(old_func_eval, my_list_copy[i])
        old_func_eval = new_func_eval
    return new_func_eval





def mymap(map_function, map_list):
    """Apply a function to each element of a list.

    Arguments:
    map_function -- the function to be applied
    map_list -- the list to which the function is applied
    Returns:
    map_list -- the list with elements that are the function evaluation of elements of the original list
    """
    map_list_copy = map_list.copy()
    for i in range(len(map_list_copy)):
        map_list_copy[i] = map_function(map_list_copy[i])
    return map_list_copy




