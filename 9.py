a = [2,3,5,7,9,13]

def binary(a):
    low = 10
    high = 14
    if len(a) == 0: #5 Repeat from step 1 until len(sequence)==0.
        return False
    else:
        mid_value = len(a)//2 #1 Find middle value of sequence.
        if a[mid_value] >= low and a[mid_value] <= high:
            return True #2 if the middle value is within the parameters
        else:
            if high < a[mid_value]: #3 If highest value is < middle value then forget about the top half of the sequence.
                return binary(a[:mid_value])
            else: #4 If highest value is > middle value then forget about the bottom half of the sequence.
                return binary(a[mid_value+1:])
	        
print(binary(a))
