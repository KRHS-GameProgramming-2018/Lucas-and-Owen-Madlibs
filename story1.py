from getInput import *

def playMadlibs():
    friend1 = getWord("Enter a Name: ",)
    numAnimals = getNumber("Enter a number: ", 7, 9)
    balls1 = getWord("Enter a plural ball name: ")
    object1 = getWord("Enter an object: ")
    verb = getWord("Enter an verb: ")
    verb2 = getWord("Enter an verb: ")
    
    output = ""
    output += "One day I was walking with my friend, " + friend1
    output += ". Suddenly " + friend1
    output += " said that they saw " + numAnimals + " " + balls1 + "."
    output +=   friend1 +" took out his " + object1 + ","
    output += " and began to " +  verb2 + " after the ball."
    output +=   friend1 + " got all "  + numAnimals + " " + balls1
    output += " The friend ran back to " + friend1 + " and " + verb + " the " + balls1
    #output += "
    
    
    return output
