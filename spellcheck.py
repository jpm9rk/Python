 # James Morrissey
 # computingID: jpm9rk
 # Checks user entered text for misspelled words

import urllib.request
spelled_word = []
text = 'start'
url = 'http://cs1110.cs.virginia.edu/files/words.txt'
file_handle = urllib.request.urlopen(url)

for line in file_handle:
    line = line.strip().decode("UTF-8")
    spelled_word.append(line)
print("Type text; enter a blank line to end. ")
while text != '':
    text = input()
    words = text.split()
    for some_word in words:
        stripped_word = some_word.strip(""".?'!",()""")
        stripped_word = stripped_word.strip('')
        lower_word = stripped_word.lower()
        if (stripped_word in spelled_word) or (lower_word in spelled_word):
            continue
        else:
            print("  MISSPELLED:", stripped_word)


