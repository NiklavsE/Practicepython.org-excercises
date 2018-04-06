import random
from random import randint 
import time
from time import sleep

def number_generator():
    r_number = ""
    for i in range(4):
        i = str(randint(0,9))
        if i not in r_number: 
            r_number += i
        else:
            number_generator()
        if len(r_number) == 4:
            return r_number
            

def user_input():
    u_number = input("Enter a 4 digit number: " )
    if len(u_number) != 4:
        print("It must be a 4 digit number!")
        user_input()
    return u_number




# cows if correct and in right pos
# bulls if correct but in wrong pos  
def cows_n_bulls(r_number):
    u_number = user_input()
    cows = 0
    bulls = 0 
    ub_num = ""
    rb_num =  ""
    length = len(u_number)
    list(r_number)
    list(u_number)
    for i in range(0,length):
        if list(u_number[i]) == list(r_number[i]):
            cows += 1
            
        else:
            ub_num += u_number[i]
            rb_num += r_number[i]
            
    if cows == 4:
        return print("You my good sir, are a winner!!")
        
    for i in range(0,len(ub_num) - 1):
        for x in range(0, len(rb_num) - 1):
            if ub_num[i] == rb_num[x]:
                bulls += 1
    


    print(" %s - cows, %s - bulls" % (cows, bulls))
    cows_n_bulls(r_number)

def intro():
    print("Welcome to the game of Bulls and Cows")
    time.sleep(1)
    print("Your task is very simple, guess a number of 4 digits!")
    time.sleep(1)
    print("But you will be given hints to help you find out the number!")
    time.sleep(0.5)
    print("You will recieve a cow for every number that is correct and in the right sequence, but a bull for every number that is one of the 4 digits, but is in the wrong position of 4 digit sequence")
    time.sleep(1)
    print("Let's begin!")
    time.sleep(1)

def game():
    print("Computer has come up with a number, try to guess it!!!")
    r_number = number_generator()
    cows_n_bulls(r_number)


def again():
    go = input("Wanna play again? (y/n): ")
    if go == "n":
        print("Thank you for playing")
    elif go == "y" :
        game()
    elif go != "y" and  "n":
        print("Enter either y or n !")
        again()
    

game()
    

