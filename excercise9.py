import random
r_num = random.randint(0,9)
def game () :
    p_choice = int(input("Take your best shot: "))
    if r_num == p_choice:
        print("You got it right!")
    else:
        print("Sorry that was incorrect!")
    again()
def again() :
    choice = input("you have another chance, do you take it (yes/no): ")
    if choice == "yes" : game()
    elif choice == "no" : print("Thank you for playing with me :)")
    else:  print("understandable, bye ;)")
game()
    
s
