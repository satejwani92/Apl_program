
f = open("sample.txt",'r')
text = f.read()
print(text)
f.close() 


# it reads only 5 char.
f = open("sample.txt",'r')
text = f.read(7)
print(text)
f.close() 