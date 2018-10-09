from getInput import *

def playMadlibs():
    friend1 = getWord("Enter a Name: ")
    number = getNumber("Enter a number: ", 80, 100)
    day = getWord("Enter a day: ")
    restuarant = getWord("Enter a restuarant: ")
    month = getWord ("Enter a month: ")
    year = getWord ("Enter a year: ")
    secondNum = getNumber("Enter a number: ", 1, 20)
    place = getWord ("Enter a place")
    loveHate = getWord ("Enter a Place")
    
    output = ""
    output +=  friend1 + " is " + number + " years old."
    output +=" Every week on " + day + ", " + friend1 + " goes to " + restuarant + "."
    output +=" Today is " + day + " the 6th, " + month + " " + year + ". It is " + friend1 + "'s " + number + "th birthday. "
    output +=  friend1 + " has " + secondNum +  " grand children. " 
    output +=" Every time " + friend1 + " wants to see his family he meets them in " + place + " ."
    output +=" All of his grand children" + loveHate + " to see him"
    
    
    return output
