seq = [1,2,3,1,2,3,4,1,2,3,4,5]

def longest_sub_sequence(seq):
    """ """
    subseq = []
    longest = []
    
    for i in range(len(seq)): #for every element in the sequence (from 0 to 15)
        #if the element is in the seq (15 elements)
        #and its value is smaller than that of the next element
        if i < len(seq) - 1 and seq[i] <= seq[i+1]:
            subseq.append(seq[i])
        else:
            subseq.append(seq[i]) #ends the subseq
            if len(longest) < len(subseq):
                longest = subseq #selects biggest subseq
                subseq = [] #resets the sequence
    print(longest)

longest_sub_sequence(seq)
