def censor(string):
    censordedwordsuppercase = ["THE", "AN", "A"]
    newstring = ""
    stringsplit = string.split(" ")
    for i in range(0, len(stringsplit)):
        lettertocheck = stringsplit[i]
        if lettertocheck.upper() in censordedwordsuppercase:
            for i in range(0, len(stringsplit[i])):
                newstring = newstring + "#"
                if i == len(lettertocheck) - 1:
                    newstring = newstring + " "
        else:
            newstring = newstring + stringsplit[i] + " "
    if newstring != string:
        newstring = newstring + " <n11081236>"
    return newstring

print(censor("The cat ate a mouse."))
