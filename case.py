## THIS PROGRAM S=DETERMINES THE CASE OF A CHARACTER INPUT USING ISUPPER AND ISLOWER FUNCTIONS

character= input("Enter a character: ")
## asks the user to input a character

if len(character) != 1:
    print("The character is more than one character long. Please use a single character")
    exit()
##if the character is more than one character long, prints an error message and exits the program

if character.isupper():
    print("The character is uppercase")
elif character.islower():
    print("The character is lowercase")
else:
    print("The character is neither uppercase nor lowercase")

