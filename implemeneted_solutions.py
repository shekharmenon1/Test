# - Solution 1 - Regular Expression and Finite State Automation (Topic 5.1)

import re
def censor(string):
    #initializing new string to display
    newstring = ""
    #finding words to censor
    x = re.findall(r'[aA][nN]?|[Tt][Hh][Ee]', string)
    #splitting passed string to edit on space to get each word
    stringsplit = string.split(" ")
    #looping through list containing words in passed string
    for i in range(0, len(stringsplit)):
        #check each word and see if it needs to be censored
        lettertocheck = stringsplit[i]
        #if word is in censored list then do editing method
        if stringsplit[i] in x:
            #add number of hastags based on lenght of word to censor
            for i in range(0, len(stringsplit[i])):
                newstring = newstring + "#"
                #add a space after every hashtag after each word is over. until it is end of string
                if i == len(lettertocheck) - 1 and i < len(stringsplit)-1:
                    newstring = newstring + " "
        #if the word need not be censored. add the word directly and add a space if words to check is not over
        else:
            newstring = newstring + stringsplit[i]
            if i < len(stringsplit)-1:
                newstring = newstring + " "
    #if the string has been modified add student number at end of modified string
    if newstring != string:
        newstring = newstring + " <n11081236>"
    #return modified string
    return newstring
#pass string to modify
print("Problem Solving Assignment Solutions\n")
print("1. Regular languages and finite state automata\n")
print(censor("The Man went to a shop with an elephant. THe Dog the cat and THE mouse were very angry like A lion."))
print("\n")

# - Solution 2 - Linear Algebra (Topic 5.2)

import numpy as np
import numpy.linalg as la
def fertiliser(an, ap, bn, bp, n, p):

    #Matrix containing proportions of Nitorgen & Phosphate within Fertilizer A & fertilizer B
    NPProportion = np.array(
        [[an, ap],
         [bn, bp]]
    )
    # One dimensional vector containing the quantiy of nitrogen (n) and quantiy of phosphate (p) required. 
    NPAmount = np.array(
        [[n],
        [p]]
    )
    #calculating the proportion needed to get to end result
    ABAmount = la.inv(NPProportion) @ NPAmount
        
    unknownproportion_values = []
    #putting the values into an array and displaying
    amount_of_a_needed = ABAmount[0][0]
    amount_of_b_needed = ABAmount[1][0]
    unknownproportion_values.append(amount_of_a_needed)
    unknownproportion_values.append(amount_of_b_needed)
    return tuple(unknownproportion_values)
    
#pass values
print("2. Linear algebra\n")
print(fertiliser(0.3, 0.2, 0.1, 0.4, 40, 60))
print("\n")
