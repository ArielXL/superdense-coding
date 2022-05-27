from printer.welcome import welcome
from printer.app_info import app_info
from printer.developments_info import developments_info

from superdense_coding.superdense_coding import *

def get_message():
    while True:
        print('\nEscriba la cadena de dos bits a transferir:', end=' ')
        msg = input()
        print()

        if len(msg) == 2 and set(msg).issubset({'0', '1'}):
            break
    return msg

def main():

    while True:

        option = welcome()

        if option == 1:
            msg = get_message()
            superdense_coding = SuperdenseCoding(msg)
            superdense_coding.superdense_coding()
        elif option == 2:
            developments_info()
        elif option == 3:
            app_info()
        else:
            return

if __name__ == '__main__':
    main()