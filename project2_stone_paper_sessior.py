import random

def gamewin(comp,you):
    if comp == you:
        return None
    elif comp == 'stone':
        if you == 'paper':
            return True
        elif you == 'sessior':
            return False
    elif comp == 'paper':
        if you == 'sessior':
            return True
        elif you == 'stone':
            return False
    elif comp == 'sessior':
        if you == 'stone':
            return True
        elif you == 'paper':
            return False
        
print("comp turn : stone, paper, sessior..?")
randNo = random.randint(1,3)
if randNo == 1:
    comp = 'stone'
elif randNo == 2:
    comp = 'paper'
elif randNo == 3:
    comp = 'sessior'
    
you = input("your turn : stone, paper, sessior..?")
a = gamewin(comp,you) 
print(f"computer choose {comp}")
print(f"you choose {you}")

if a == None:
    print("game is tie..!")
elif a:
    print("you win..!")   
else:
    print("you loose..!")
    