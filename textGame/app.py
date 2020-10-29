import random
from os import system, name

questionsList = []
answersList = []
health = 100

def clearConsole():
    if name == 'nt':
        _ = system('cls')
    else: 
        _ = system("clear")

def healthDamage( damage ):
    global health
    print("You take " + str(damage) + " points of damage! You have " + str(health) + " health left.")

def newLine(): 
    print("")

def appendAnswer( answer ):
    global answersList
    answersList.append(answer)

def appendQuestion( question ):
    global questionsList
    questionsList.append(question)

def randomInt( min, max ):
    return random.randint(min, max)

def pressEnter():
    input("Press Enter to continue.")

def healthCheck( damage ):
    global health
    health = health - damage
    if health <= 0:
        print("You have died")
    else:
        healthDamage(damage)

def choiceCreation( choicesList ):
    for choice in choicesList:
        index = choicesList.index(choice)
        choiceNumber = index + 1
        print("[" + str(choiceNumber) + "] " + choice)

def start():
    print("Hello! Welcome to my game.")
    name = input("Let's start by inputting your name: ")
    print("Nice to meet you " + name + ". What a lovely name.")
    appendAnswer(name)
    appendQuestion("Let's start by inputting your name")
    pressEnter()
    wake_up(name)

def wake_up( name ):
    clearConsole()
    print("You slowly open your eyes. The TV is still playing low from when you fell asleep the night before.")
    print("Looking around the room you see it. Your dog! ")
    print("Which action do you take? ")

    choices = ["Call him over", "Leave him be, he looks peaceful"]
    choiceCreation(choices)

    dog_choice = input("(Input a number between 1 and 2) ")

    appendQuestion("Do you call your dog?")
    appendAnswer(choices[int(dog_choice - 1)])

    if dog_choice == "1":
        dog()
    else:
        print("Let's go to the bathroom")
        pressEnter()
        bathroom()

def dog():
    print("You call Benji over. He runs and jumps on the bed.")
    print("Which action do you take?")

    choices = ["Pet him", "Give him a kiss", "Do nothing"]
    choiceCreation(choices)

    dog_choice = input("(Input a number between 1 and 3) ")

    appendQuestion("How do you care for your dog?")
    appendAnswer(choices[int(dog_choice - 1)])

def bathroom():
    print("bathroom")

clearConsole()
start()