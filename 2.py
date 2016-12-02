n = int(input("Please insert a factorial number: "))

def Zeroes(n):
    """A function that returns the number of trailing zeroes from a fractorial number"""
    if n >= 5: #If the factorial number is higher or equal to 5
        return Zeroes(n/5) + n/5 #returns the function with a decreasing value
    else:
        return 0 #if n is lower than 5 then it is returned as 0

print(Zeroes(n))
