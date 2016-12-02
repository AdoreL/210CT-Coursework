S = "This is awesome"

def Rev(S):
    '''Takes a sentance and reverses it'''
    
    Spl = S.split(" ") #Splits the sentance
    A = [] #Creates an empty array
    for i in range(len(Spl) - 1, -1, -1):
        # from range of length -1, until -1, reduces range by 1
        A.append(Spl[i])
    return " ".join(A) #joins the elements in the array with a space inbetween

print(Rev(S))
