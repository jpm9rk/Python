# James Morrissey
# computingID: jpm9rk
# Parsing of information from Virginia state salaries data

import re
import urllib.request


job = re.compile(r'Job title: ((\S| )*)<')
salary = re.compile(r'paytype.amount, ([0-9]+)')
rank = re.compile('University of Virginia rank<\/td><td>(([0-9]|,)*)')
doesnt_exist = False

def name_to_url(name):
    """
    Return url corresponding to given name.

    :param name:(str) name of individual
    :return: base_url + name (str). url associated with name
    """
    new_name_list = []
    url_name = ''
    base_url = "http://cs1110.cs.virginia.edu/files/uva2018/"
    name = name.replace('.','')
    if ',' in name:
        new_name = name.split(',')
        new_name_list.append(new_name[1])
        new_name_list.append(new_name[0])
        yes_comma = True
        no_comma = False
    for i in range(len(new_name_list)):
        new_name_list[i] = new_name_list[i].strip()
    if ',' not in name:
        new_name_list = name.split(' ')
        no_comma = True
        yes_comma = False
    if yes_comma:
        first_new_name_list = new_name_list[0].split()
        for word in first_new_name_list:
            url_name += word.lower() + '-'
        url_name += new_name_list[1].lower()
    if no_comma:
        for word in new_name_list:
            word = word.lower()
            url_name += word + '-'
        url_name = url_name[:-1]
    return base_url + url_name

def report(name):
    """
    Return job description, salary, and pay rank.

    :param name:(str) name of individual who information about is desired
    :return: job_description_string (str), float(salary_string), job_rank (int)
    """
    global doesnt_exist

    url = name_to_url(name)
    job_rank = 0
    try:
        stream = urllib.request.urlopen(url)
    except:
        job_description_string = None
        salary_string = '0'
        job_rank = 0
        doesnt_exist = True
    if not doesnt_exist:
        for line in stream:
            decoded = line.decode('utf-8').strip()
            job_description = job.search(decoded)
            if job_description:
                job_string = job_description.group(1)
                job_description_string = re.sub("&#39;", '\'', job_string)  # returns a string
                job_description_string = re.sub("&amp;", "&", job_description_string)  # returns a string
        stream.close()

        stream = urllib.request.urlopen(url)
        for line in stream:
            decoded = line.decode('utf-8').strip()
            salary_description = salary.search(decoded)
            if salary_description:
                salary_string = salary_description.group(1)
        stream.close()

        stream = urllib.request.urlopen(url)
        for line in stream:
            decoded = line.decode('utf-8').strip()
            rank_description = rank.search(decoded)
            if rank_description:
                if rank_description.group(1):
                    job_rank_no_comma = rank_description.group(1).replace(',', '')
                    job_rank = int(job_rank_no_comma)
        stream.close()


    return job_description_string, float(salary_string), job_rank










