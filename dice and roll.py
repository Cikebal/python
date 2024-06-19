import random     # This 'import' the random module which will be used in the programme 

#Variables 

# A variable is a container for storing data values. It is like a box to store something 
# The variable 'win' stores how many time you win in the game if you continue play the game. 


win=0         
lose=0
draw=0

def intro():

    print("You are playing dice and roll".center(50, "-"))
    print("Win if u have a bigger number, lose if u have a small number")

    input("press enter to continue")   # Allows user to 'input' info but because it is not tied to a variable 
                                        
def game():
    print("Rolls first dice")
    first_roll=random.randint(1,12)   # 'randint' is an example of a method.
    print( "First dice rolls = ",first_roll)  #  to an object is random
    input("press enter to continue")  # continue for your dice roll
    your_roll=random.randint(1,12)
    print("Your roll = ",your_roll)
    input("press enter to continue")

    while first_roll == your_roll:
        print("It is a draw,play again")# when draw, need to play again.
        global draw
        draw+=1
        game()
    if first_roll > your_roll:
        print("Your number is smaller, You LOSE !!!!!") #if your number is small
        global lose         # We use the global keyword to read and write a global variable inside a function.
        lose+=1
        

    if your_roll > first_roll:
        print("Your number is bigger, You WIN !!!!")# if your number is higher
        global win
        win+=1

    print("game won:  "+str( win)+" lose:  "+str(lose)+" draw:  "+str(draw))  # We need to convert the variables to string format for us to print them  
    play_again = input("Play again? (yes/no)")
    play_again= play_again.lower()

    if play_again =="no":                               # Simple example of if, else statement.  If you type in 'no' it will quit the game
        input("Good bye, press enter to quit ")         # 'else' it will reinvoke the intro and game function hence repeating the game        

    else:
        intro()                              
        game()

intro()         # A function will need to be 'called'/invoked before it does anything, eg: intro(),game()  
game()                                  

