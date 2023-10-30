import re
a = "this is a pyhton program portal"
match= re.search('portal',a)
print('start index',match.start())
print('end index',match.end())
print(match)