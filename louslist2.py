# James Morrissey
# computingID: jpm9rk

import urllib.request
def instructors(department):
    instructors = []
    department_teachers = {}  # a dictionary with department as key, and list of instructors as value
    url = "http://cs1110.cs.virginia.edu/files/louslist/" + department  # set url to be the url
    file_handle = urllib.request.urlopen(url)  # create a file handle to reference the url
    for stream in file_handle:
        line = stream.decode("UTF-8").strip().split('|')  # split each line in the file based on |
        if "+" in line[4]:
            line[4] = line[4].strip("+123456789")
        # print(line)
        if department in department_teachers.keys():
            if line[4] in department_teachers[department]:
                continue
            else:
                # if the department already exists in the dictionary
                department_teachers[department].append(line[4])
        else:  # if the department not already in dict, create a new key with that department
            department_teachers[department] = [line[4]]
        # print(department_teachers[department])
    department_teachers[department].sort()
    # print(department_teachers)
    return department_teachers[department]



