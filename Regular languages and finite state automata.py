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
print(censor("Dog Cat Mouse"))