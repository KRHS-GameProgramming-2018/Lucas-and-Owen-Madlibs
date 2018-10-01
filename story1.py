from getInput import *

def playMadlibs():
    friend1 = getWord("Enter a Name: ",)
    numAnimals = getNumber("Enter a number: ", 7, 9)
    balls1 = getWord("Enter a plural ball name: ")
    object1 = getWord("enter an object: ")
    
    output = ""
    output += "One day I was walking with my friend, " + friend1
    output += ". Suddenly " + friend1
    output += " said that they saw " + numAnimals + " " + balls1 + "."
    output += " The friend took out his " + object1 + ","
    output += " and began to chase after the ball."
    output += " The friend got all "  + numAnimals + " " + balls1
    
    
    
    
    return output
