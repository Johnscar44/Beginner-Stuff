command = ""
started = False
stopped = True
while True:
    command = input("\nWhat would you like the car to do?\nEnter 'help' for help or 'q' to quit\n ").lower()
    if command == "start":
        if started:
            print('car is already running')
        else:
            started = True
            print('you started the car')
    elif command == "stop":
        if stopped:
            print('im stopped already')
        else:
            stopped = False
            print('We pulled over..')
    elif command == "go":
        print('we are moving the fuck out')
    elif command == "help":
        print("""
get in - to get in the car
start - to start the car
go - move the fuck out
stop -stop the car
quit - ditch this hot car and bail
    """)
    elif command == "get in":
        print('get in the damn car')
    elif command == "q":
        print('ditch this hot car and bail bro')
        break
    else:
        print('i dont know what the fuck your saying dude?')

import cheekycat

def main():
    cheekycat.cheekycat('My neck')
    cheekycat.cheekycat('My back')
    cheekycat.cheekycat('lick my pussy... get it?')
    cheekycat.cheekycat('and my crack')
    cheekycat.cheekycat('Goodbye!')

if __name__ == '__main__':
        main()
