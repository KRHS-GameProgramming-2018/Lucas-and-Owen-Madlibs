from screens import *
from getInput import *
import story1
import story2
import story3
import story4

print showSplash()
raw_input("Press Enter to Start")

go = True
while go:
    print showMenu()
    response = getMenuInput()
    if response == "Q":
        go = False
        print"Thanks for playing"
    elif response == "1":
        print story1.playMadlibs()
        raw_input("Press Enter to Continue")
    elif response == "2":
        print story2.playMadlibs()
        raw_input("Press Enter to Continue")
    elif response == "3":
        print story3.playMadlibs()
        raw_input ("Press input to continue")
    elif response == "4":
        print showEasterEggImage()
        print story4.playMadlibs()
        raw_input("Press Enter to Continue")
    else:
        print "Please pick a valid option!"
        
        

