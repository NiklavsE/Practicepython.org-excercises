def Prime():
    print("It is a prime number")
def Prime_not():
    print("It is not prime number")

def Prime_test():
        number = int(input("Enter a number: "))
        if number == 2:
            return Prime()
            
        PN_score = 0
        for num in range(2,number - 1): 
           if number % num != 0 and number != num: PN_score += 1
           
        #print(PN_score)
        if PN_score == number - 3:
            return Prime()
        else:
            return Prime_not()

                

Prime_test()
    
