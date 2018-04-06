def Fibonaci():
    
    list_index = int(input("how many numbers: "))
    if list_index == 0:
         fib = []
    elif list_index == 1:
        fib = [1]
    elif list_index == 2:
        fib = [1,1]
    if list_index > 2:
        fib = [1,1]
        for i in range(1, list_index - 1):
            fib.append(fib[i -1] + fib[i])
    return fib
    
print(Fibonaci())

        
