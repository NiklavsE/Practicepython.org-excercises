
def Set_list(): 
    A_list = [1,1,2,2,3,3,4,4,5,5]
    B_list = set()
    index = int(len(A_list))
    for i in range(0,index):
        B_list.add(A_list[i])
    return B_list




print(list(Set_list()) )
                   
