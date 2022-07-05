#import graphs
#import digraphs

# You can define some helper functions here if you like!
#defining function to check if only one pegleft

#Global lsit variable to hold the Board moves. 
path = []

#Check if more than one peg remaining in the Board
def Isonepeg(Board):
    #initialize counter and flag
    onex = False
    countx = 0
    #looping through game board
    for x in range(0, len(Board), 1):
        #appending when find peg
        if Board[x] == "X":
            countx = countx + 1
    #setting flag to true when peg found
    if countx == 1:
        onex = True
    return onex

#Find if a pattern is found returns the index in the GameBoard
def Patternfound(Board, pattern):
    #initialize index to null
    index = -1
    #search for pattern
    for x in range(0,len(Board)-len(pattern)+1,1):
        #when pattern found return the index
        if (Board[x:x+len(pattern)] == pattern):
            index = x
            break
    return index

#Moves the peg in the board
def move(Board):
    #initializing newboard
    newBoard=""
    #first checking if 'XXO' pattern exists
    pattern = "XXo"
    newpattern = "ooX"
    index = Patternfound (Board,pattern)
    #adding what is already in the gameboard if no pattern is found
    if (index != -1):
        
        for i in range (0, index,1):
            newBoard = newBoard + Board[i]
        for i in range (0,3,1):
            newBoard = newBoard + newpattern[i]
        for i in range(index+3, len(Board),1):
            newBoard = newBoard + Board[i]
        path.append((index, "R"))
        #displaying path moved
        print ("path = (",index,"R)")
    #when patter found making adjustments based on pattern
    else:
        #next checking if 'oXX' pattern exists
        pattern = "oXX"
        newpattern = "Xoo"
        index = Patternfound (Board,pattern)
        if (index != -1):
            for i in range (0, index,1):
                newBoard = newBoard + Board[i]
            for i in range (0,3,1):
                newBoard = newBoard + newpattern[i]
            for i in range(index+3, len(Board),1):
                newBoard = newBoard + Board[i]
            path.append((index+2, "L"))
            #displaying path moved
            print ("path = (",index+2,"L)")
               
        else:
            #return current board if no pattern return regular board
            return Board       
    #return newboard
    return newBoard
    

def pegsSolution(Board):
    # Program your solution here
    #initializing path array
    path.clear()
    #print gamboard
    print ("\nGameBoard = ",Board);
    
    #initializing new board string
    while Isonepeg(Board) != True:
        newBoard = move (Board)
        print ("new Board =", newBoard)
        if (Board == newBoard):
            print ("Board is not solvable; exiting")
            break
        else:
            Board = newBoard
    return path
    
        
## TEST HARNESS
# The following will be run if you execute the file like python3 pegs_n1234567.py
# Your solution should not depend on this code.
# You may wish to add your own test cases.
if __name__ == '__main__':
    gameBoard = 'XoXX' # should return [(3, 'L'), (0, 'R')]
    print(pegsSolution(gameBoard))
    gameBoard = 'XXoXoXo' # should return [(3, 'L'), (0, 'R')]
    print(pegsSolution(gameBoard))