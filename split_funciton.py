file = open('sample.txt','r')
data = file.readlines()
for line in data:
    word = line.split()
    print(word)

file = open('another.txt','r')
data = file.readlines()
for line in data:
    word = line.split()
    print(word)