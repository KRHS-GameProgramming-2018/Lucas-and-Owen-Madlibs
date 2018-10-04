from getInput import *

def playMadlibs():
    friend1 = getWord("Enter a Name: ",)
    numAnimals = getNumber("Enter a number: ", 7, 9)
    balls1 = getWord("Enter a plural ball name: ")
    object1 = getWord("Enter an object: ")
    verb = getWord("Enter an verb: ")
    adverb = getWord("Enter an adverb ending in ly: ")
    day = getWord("Enter a day: ")
    food = getWord("Eter a food: ")
    wordEndsInED = getEd ("Enter a word that ends in ed:")
    
    output = ""
    output += "One day I was " + adverb + " with my friend, " + friend1
    output += ". Suddenly " + friend1
    output += " said that they saw " + numAnimals + " " + balls1 + "."
    output +=   friend1 +" took out his " + object1 + ","
    output += " and began to run after the balls. "
    output +=   friend1 + " got all "  + numAnimals + " " + balls1 + ". "
    output += " Then " + friend1 + " ran back to friend and gave them the " + balls1 + ". "
    output += " The friend then said, thank god it's " + day + ". "
    output += " The friend said to " + friend1 + " lets go get some " + food + "."
    output += " They walked to the store for the " + food + " and " + wordEndsInED + " trying the food."
    
    return output
