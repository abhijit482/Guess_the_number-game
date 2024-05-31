 
TRAIN = '''

   ___                                             _____   _                        _  _                    _                      
  / __|   _  _     ___     ___     ___      o O O |_   _| | |_      ___      o O O | \| |   _  _    _ __   | |__     ___      _ _  
 | (_ |  | +| |   / -_)   (_-<    (_-<     o        | |   | ' \    / -_)    o      | .` |  | +| |  | '  \  | '_ \   / -_)    | '_| 
  \___|   \_,_|   \___|   /__/_   /__/_   TS__[O]  _|_|_  |_||_|   \___|   TS__[O] |_|\_|   \_,_|  |_|_|_| |_.__/   \___|   _|_|_  
_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| {======|_|"""""|_|"""""|_|"""""| {======|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 

'''
import random


number = random.randint(1,100)
print(number)
level_entry = False
print(TRAIN)

#Enter Proper input
while level_entry == False:
    loop = input("Enter the level of Dificulty you want:'Hard' or 'Easy':  ").lower()

    if loop == 'hard':
        attempt = 5
        level_entry = True
    elif loop == 'easy':
        attempt = 10
        level_entry = True
    else:
        print("Enter Proper level")

print(f"Your Number of attempt is {attempt} \nGuess between 1 to 100:")

won = False
for try_ in range(1,attempt+1):
    guess = int(input("Enter Your Guess: "))
    if guess > number:
        print(f"Value too high, attempt left :{attempt-try_}")
    elif guess < number:
        print(f"Value too low, attempt left :{attempt-try_}")
    elif guess == number:
        print(f"You Won correct Guess:{guess}")
        won = True
        break

   

if won== False:
    print("You lost all your attempt, try decrease level")



