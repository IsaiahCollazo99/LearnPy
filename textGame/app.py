def start():
    print("Hello! Welcome to my game.")
    name = input("Let's start by inputting your name: ")
    print("Nice to meet you " + name + ". What a lovely name.")
    input("")
    wake_up(name)

def wake_up( name ):
    print("You slowly open your eyes. The TV is still playing low from when you fell asleep the night before.")
    print("Looking around the room you see it. You're dog! ")
    print("[1] Call him over")
    print("[2] Leave him be, he looks peaceful")
    dog = input("Which action do you choose? ")
    if int(dog) == 1:
        print("Come here Benji!")
    else:
        print("Let's go to the bathroom")

start()
