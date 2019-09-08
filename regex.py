# James Morrissey
# computingID: jpm9rk

import re

nospace = re.compile(r"\S+")
quotation = re.compile(r'("\S(\w|\s|,|\.|\?|!|-)+\S")|("\S")|("[0-9]+")|("\S+")')
twonum = re.compile(r'(-?[0-9]+(\.[0-9]+)?)(,|, | )(-?[0-9]+(\.[0-9]+)?)')
