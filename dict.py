import re

s = open("cs_CZ.txt", "r")
s = s.read ()

s = re.sub(r'\/.+$', r'', s, flags = re.MULTILINE)
with open('cs_CZ_1.txt', 'w') as f:
            f.write(s)
