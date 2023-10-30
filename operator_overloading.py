num1 = 10
num2 = 20                              #here only addtition has been done using + operater
print(num1 + num2)                       
print(num1.__add__(num2))
print(int.__add__(num1,num2))
print(dir(int))

#another
num1 = "hello"
num2 = "world"                          #here concatinated two string using + operater
print(num1 + num2)                       
print(num1.__add__(num2))
print(str.__add__(num1,num2))
print(dir(str))

#another
class Book:
    def __init__(self,title,pages):
        self.title = title
        self.pages = pages                      #here we if we use object as b1 & b2
        
b1 = Book('ones indian girl',300)
b2 = Book('making india awesome',200)
print('the total number of pages is',b1.pages + b2.pages)        

#here if we dont want to add object to the pages then
class Book:
    def __init__(self,title,pages):
        self.title = title
        self.pages = pages                     
    def __add__(self,other):
        self.pages+other.pages     
b1 = Book('ones indian girl',300)
b2 = Book('making india awesome',200)
print('the total number of pages is',b1 + b2) 