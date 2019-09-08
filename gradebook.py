# James Morrissey
# computingID: jpm9rk
# Program to keep track of running total and cumulative weight for each grade type, and return overall grade


dict_grades = {}  # should store the type of assignment and its grade * weight
dict_weight = {}  # should store the type of assignment and its weight
dict_averages = {}  # stores avg to that point for that type of assignment



def assignment(kind, grade, weight = 1):
    """
    Update running total of grade values, weights, and averages for particular assignment type.

    :param kind:(string) the type of assignment
    :param grade: (float) the grade on a particular assignment
    :param weight: (float) the weight of a particular assignment
    :return: None
    """
    global dict_grades
    global dict_weight
    global dict_averages
    grade_total = 0  # reset calculation of the sum of the grades for assignments of that type
    weight_total = 0  # reset the calculation for the total weight for assignments of that type
    if kind in dict_grades.keys():  # if there's already a dictionary key for assignment type
        dict_grades[kind].append(grade * weight)  # add another grade to the total for type of assignment
        dict_weight[kind].append(weight)  # add another weight for type of assignment
    else:
        dict_grades[kind] = [grade * weight]  # if assignment type doesn't exist then make it
        dict_weight[kind] = [weight]  # if assignment type doesnt exist then make it
    for grade_value in dict_grades[kind]:  # sum up all the grade values for assignment type
        grade_total += grade_value
    for weight_value in dict_weight[kind]:  # sum up all weight values for assignment type
        weight_total += weight_value
    dict_averages[kind] = grade_total / weight_total  # 'avg' for assignment type


def total(proportions):
    """
    Return the value of your grade based on specified proportions for assignment types.

    :param proportions:(dict) dictionary specifying proportion for each assignment type
    :return:(float) the value of your final grade
    """
    your_grade = 0.0
    for key in dict_averages.keys():  # iterate over the types of assignments
        if key in proportions.keys():  # if that type of assignment exists
            your_grade += proportions[key] * dict_averages[key]  # add to grade the proportion times average
    return your_grade









