import os
from translator import TEXT_TO_MORSE
clear_screen = lambda: os.system('cls')

def main():
    # Run the program until the user decides to stop 
    while True:
        clear_screen()
        input_string = input("Type the sentence you want to translate:\n").lower()
        output_string = ""
        # Iterate through all characters of the input string
        for char in input_string:
            if char in TEXT_TO_MORSE:
                output_string += TEXT_TO_MORSE[char]
                if char != " ":
                    output_string += " "
        print("\nTranslated Morse Code text:\n" + output_string + "\n")
        go_again = input("Do you want to translate more text?\nType 'no' if you want to exit, otherwise the program will continue: ").lower()
        
        if go_again == "no":
            break
        
if __name__ == '__main__':
    main()