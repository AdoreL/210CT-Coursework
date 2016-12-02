n = int(input("Insert a positive integer: "))

def Perf_Sq(n):
    """function that returns highest perfect square which is less or equal to n"""
    S = 0 #new open value
    for i in range(1, n): #for element in range 1 to n
        PF = i * i #perfect square equal so i^2
        if PF <= n: #if the perfect square is equal or less to input
            S = PF #open value aquires perfect square value
        else: #if perfect square is higher than n
            break #stops, returning previous highest value
    print("The highest perfect square is: " + str(S))
    
Perf_Sq(n)
