
with open('another.txt','r') as f:
    a = f.read()
print(a)

with open('another.txt','w') as f:
    a = f.write("good morning here im we have to go.")
print(a)