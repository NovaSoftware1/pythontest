# I used the time.sleep() command to make the code stop for a certain amount of time


# I used import to import libraries that add extra functionality
from datetime import date
import time

# I used the print() command to display text in the command line
print("Welcome To Nobara CLI Edition")
print("This is totally the real version of Nobara Linux")

# I created a variable to initialize the input() function
command = input("root@thispc: ")

# I used many if statments to tell the code what to do depending on the command entered
if command == "time":
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print("The Time Is ", current_time)
    print("You have 100 seconds to restart to choose another command or the program will just end")
    time.sleep(100)

if command == "date":
    today = date.today()
    print("The Date Is ", today)
    print("You have 100 seconds to restart to choose another command or the program will just end")
    time.sleep(100)

if command == "mind_reader.fake":
    number = input("Pick A Number And Type It Here: ")
    time.sleep(1)
    print("Scanning Brainwaves... 5%")
    time.sleep(0.6)
    print("Scanning Brainwaves... 90%")
    time.sleep(1)
    print("Translating Brainwaves Into Binary...")
    time.sleep(3)
    print("Your Number Was: ", number)
    print("You have 100 seconds to restart to choose another command or the program will just end")
    time.sleep(100)

if command == "game":
    print("Game Loading...")
    time.sleep(3)
    print("Game Loaded!")
    time.sleep(2)
    print("You are stranded on a deserted island. You only have 3 options. Escape, become one with the ocean or turn the island into an oil rig.")
    gameChoice = input("Which will you choose: ")
    time.sleep(2)
    print("You have decided to ", gameChoice)
    time.sleep(2)
    print("Game crashed because luke cant be bothered to write anymore code")
    time.sleep(1)
    print("You have 100 seconds to restart to choose another command or the program will just end")
    time.sleep(100)



