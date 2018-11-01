from getInput import *

def playMadlibs():
    realName = getWord ("Enter your real first and last name: ")
    friend1 = getWord("Enter a male name: ")
    number = getNumber("Enter a number: ", 84, 90)
    day = getWord("Enter a day of the week: ")
    restuarant = getWord("Enter a restuarant: ")
    month = getWord ("Enter a month: ")
    year = getWord ("Enter a year: ")
    secondNum = getNumber("Enter a number: ", 5, 19)
    place = getWord ("Enter a state in the USA: ")
    loveHate = getWord ("Enter the word love or hate: ")
    nameEndingInY = getY ("Enter a women's name ending in Y: ")
    food = getWord ("Enter a food: ")
    job = getWord ("Enter a job: ")
    bookGenre = getWord ("Enter a book Genre: ")
    bowlingBingo = getWord ("Enter the word bowling or bingo: ")
    
    output = ""
    output +=  friend1 + " is " + number + " years old." # putting several concatenations on one line can make it harder to debug
    output +=" Every week on " + day + ", " + friend1 + " goes to " + restuarant + " and orders " + food + "."
    output +=" Today is " + day + " the 6th, " + month + " " + year + ". It is " + friend1 + "'s " + number + "th birthday. "
    output +=  friend1 + " has " + secondNum +  " grand children." 
    output +=" Every time " + friend1 + " wants to see his family he meets them in " + place + "."
    output +=" All of his grand children " + loveHate + " seeing him. "
    output +=  friend1 + " also has a wife named " + nameEndingInY + ". " + nameEndingInY + " is " + number + " too. "
    output +=  friend1 + " and " + nameEndingInY + " are both retired, they used to work as " + job + "'s ."
    output +=" Now they spend their time reading " + bookGenre + " books and enjoy going " + bowlingBingo + " from time to time."
    output +=" The story is now over, thanks for playing " + realName + ". "
    
    return output
