from getInput import *

def playMadlibs():
    friend1 = getWord("Enter a Name: ",)
    umAnimals = getNumber("Enter a number: ", 1, 100)
    day = getWord("Enter a day: ",)
    fastFoodRestuarant = getWord("Enter a fast food restuarant: ")
    
    
    output = ""
    output += friend1 + " is " + umAnimals + " years old. "
    output +=" Every week on " + day + ", " + friend1 + " goes to " + fastFoodRestuarant + "."
    
    return output
