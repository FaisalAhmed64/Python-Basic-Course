command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car is already started")
        else:
            started = True
            print(" car started")
    elif command == "stop":
        if not started:
            print("the is already stopped..")
        else:
            print("car stopped..")
    elif command == "help":
        print("""
start- to start the car
top- to stopped
quit-to exit
         """)
    elif command == "quit":
        break
    else:
        print("sorry i don't understand")
