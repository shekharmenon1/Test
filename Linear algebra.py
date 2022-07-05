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
print(fertiliser(0.3, 0.2, 0.1, 0.4, 40, 60))