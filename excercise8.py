import time 
from random import randint
print("Akmens šķēres papīrītis. Vienkārša spēle, bet vai TU vari pievieikt savu datoru? :")
time.sleep(2)
def game() : 
    game = True 
    while game is True: 
        #choices = [ "rock", "papers", "scissors"]
        c_choice = randint(0, 2)
        if c_choice == 0: opponent = "akmens"
        if c_choice == 1: opponent = "papīrs"
        if c_choice == 2: opponent = "šķēres"
        p_choice = input("Ievadi - akmens, šķēres vai papīrītis: ")
        #Opponent = choices[index(c_choice)]
        time.sleep(2)
        print("Dators izvēlas  -  %s"  % opponent )
        time.sleep(1)
        if p_choice == opponent:
            print(" Tas ir neizšķirts! ")
            break 
                    
        elif p_choice == "akmens" and opponent == "šķēres":
            print("Tu uzvarēji!")
            break
            
        elif p_choice == "šķēres" and opponent == "akmens" :
            print("Tu zaudēji!")
            break
                         
        elif p_choice == "šķēres" and opponent == "papīrs":
            print("Tu uzvarēji!!")
            break
                                
        elif p_choice == "papīrs" and opponent == "šķēres" :
            print("You lost!")
            break
                              
        elif p_choice == "papīrs" and opponent == "akmens" :
            print("Tu uzvarēji!")
            break
                                
        elif p_choice == "akmens" and opponent == "papīrs" :
            print("You lost!")
            break
        else:
            print("Neievadīji pareizi! :/")
            break
def again() :
    goAgain = input('Mēģināsi vēlreiz? jā/nē: ')
    if goAgain == "nē":
        print ("Paldies par spēli! :)")
        
    elif goAgain == "jā" :
        game()
    
game()
again()
    

