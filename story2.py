from getInput import *

def playMadlibs():
    friend1 = getWord("Enter a Name: ")
    umAnimals = getNumber("Enter a number: ", 10, 100)
    day = getWord("Enter a day: ")
    restuarant = getWord("Enter a restuarant: ")
    month = getWord ("Enter a month: ")
    year = getWord ("Enter a year: ")

    
    output = ""
    output += friend1 + " is " + umAnimals + " years old."
    output +=" Every week on " + day + ", " + friend1 + " goes to " + restuarant + "."
    output +=" Today is " + day + " " + month + " " + year + ". it is " + friend1 + "'s" + umAnimals + "th birthday"
    
    return output
