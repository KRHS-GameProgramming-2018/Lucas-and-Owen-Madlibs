from getInput import *

def playMadlibs():
    friend1 = getWord("Enter a Name: ")
    number = getNumber("Enter a number: ", 84, 90)
    day = getWord("Enter a day: ")
    restuarant = getWord("Enter a restuarant: ")
    month = getWord ("Enter a month: ")
    year = getWord ("Enter a year: ")
    secondNum = getNumber("Enter a number: ", 5, 19)
    place = getWord ("Enter a state in the USA: ")
    loveHate = getWord ("Enter the word love or hate: ")
    nameEndingInY = getY ("Enter a women's name ending in Y: ")
    food = getWord ("Enter a food: ")
    
    output = ""
    output +=  friend1 + " is " + number + " years old."
    output +=" Every week on " + day + ", " + friend1 + " goes to " + restuarant + " and orders " + food + "."
    output +=" Today is " + day + " the 6th, " + month + " " + year + ". It is " + friend1 + "'s " + number + "th birthday. "
    output +=  friend1 + " has " + secondNum +  " grand children." 
    output +=" Every time " + friend1 + " wants to see his family he meets them in " + place + "."
    output +=" All of his grand children " + loveHate + " seeing him. "
    output +=  friend1 + " also has a wife named " + nameEndingInY + ". " + nameEndingInY + " is " + number + " too. "
    
    return output
