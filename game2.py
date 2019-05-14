command = ""
while True:
    command == input('< ').lower()
    if command == "start":
        print('car has started')
    elif command == "stop":
        print('car has stopped')
    elif command == "go":
        print('we are moving the fuck out')
    elif command == "help":
        print("""
start - to start the car
go - move the fuck out
stop -stop the car
quit - ditch this hot car and bail
    """)
    elif command == "quit":
        print('ditch this hot car and bail bro')
        break
else:
    print('i dont know what the fuck your saying dude?')
