import re

s = 'Department: A computer science portal for computer science department'

match = re.search(r'portal', s)

print('Start Index:', match.start())
print('End Index:', match.end())

#\backslash

import re
 
s = 'computer.computer_science'
 
# without using \
match = re.search(r'.', s)
print(match)
 
# using \
match = re.search(r'\.', s)
print(match)

#squarebracket[]
import re

string = "The quick brown fox jumps over the lazy dog"
pattern = "[a-m]"
result = re.findall(pattern, string)

print(result)

#^ – Caret
import re

# Match strings starting with "The"
regex = r'^The'
strings = ['The quick brown fox', 'The lazy dog', 'A quick brown fox']
for string in strings:
	if re.match(regex, string):
		print(f'Matched: {string}')
	else:
		print(f'Not matched: {string}')


#$ – Dollar
import re

string = "Hello World!"
pattern = r"World!$"

match = re.search(pattern, string)
if match:
	print("Match found!")
else:
	print("Match not found.")


#. Dot
import re

string = "The quick brown fox jumps over the lazy dog."
pattern = r"brown.fox"

match = re.search(pattern, string)
if match:
	print("Match found!")
else:
	print("Match not found.")



