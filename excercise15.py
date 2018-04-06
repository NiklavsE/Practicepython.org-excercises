#Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

def Word_reverse(x):
    Word = x.split(" ")
    for i in reversed(Word):
        print(i, end=" ") 
    
    
        
        

x = input("Enter a sentence to reverse: ")
Word_reverse(x)
