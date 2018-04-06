password_database = []
import random
from random import randint

def Pass_word_Gen():
    P_length = 8
    B_Chars = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    L_Chars = 'qwertyuiopasdfghjklzxcvbnm'
    Numbers = '1234567890'
    Spec = '!@#$%^&*()<>?'
    #list_LC = list(L_Chars)
  #  list_N = list(L_Chars)
  #  list_S = list(Spec)
    pasword = ""
    for i in range(2):
        pasword += random.choice(B_Chars)
        pasword += random.choice(L_Chars)
        pasword += random.choice(Numbers)
        pasword += random.choice(Spec)
    password_database.append(pasword)
    if len(password_database) != len(set(password_database)):
        password_database.remove(password)
        Pass_word_Gen()
        
    return pasword
print(Pass_word_Gen())
print(Pass_word_Gen())
print(password_database) 

    
