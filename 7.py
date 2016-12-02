n = 11 
i = n - 1
def prime(n,i):
    if i == 1: #base case
        return ("is prime")
    elif n%i == 0: #condition, if its a perfect division then its not prime
        return ("is not prime")
    else: #if its not a perfect division then search for next smallest number
        return prime(n, i-1)
        
print(prime(n,i))
