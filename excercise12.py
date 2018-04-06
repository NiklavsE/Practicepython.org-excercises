import random 
from random import randint 

def List_creation():
    number = randint(1,9)
    a = random.sample(range(100), number)
    print(a)
    print(a[0])
    last_index = len(a) 
    print(a[last_index -1])
    




List_creation()
               
