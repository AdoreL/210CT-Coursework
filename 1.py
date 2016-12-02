array = [1,2,3,4,5,6,7,8,9,10]

import random #Imports the random function in python

def Randomize(array):
    """Creates a function that randomizes an array by removing a random element at a time and then adding them into another array"""    
    RandArray = [] #Creates a separate array that will be returned
    for i in range(len(array)): #for every element in the range of the length of the original array
        element = random.choice(array) #Uses the random:choice function to choose which element will be removed
        array.remove(element) #Removes the randomly chosen element from the original array
        RandArray.append(element) #Adds this element into the new array
    print("The new random array: ",RandArray) #After the loop is finished this prints the new randomized array

Randomize(array)
