from getInput import *

def playMadlibs():
    friend1 = getWord("Enter a Name: ",)
    numAnimals = getNumber("Enter a number: ", 7, 9)
    animals1 = getWord("Enter a ball name: ")
    object1 = getWord("enter an object: ")
    
    output = ""
    output += "One day I was walking with my friend, " + friend1
    output += ". Suddenly " + friend1
    output += " said that they saw " + numAnimals + " " + animals1
    output += " The friend took out his " + object1
    
    
    
    
    return output
