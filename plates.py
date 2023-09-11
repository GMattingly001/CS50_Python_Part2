"""
Author: George Mattingly
Date Created: 09/09/23
Date Last worked on: 09/09/23
Vanity Plates: In Massachusetts, it's possible to request a vanity
license plate for a car that can include letters and numbers. This
project checks the validity of the license plate based on several
requirements: It must start with 2 letters, it must be between 2 and 6
characters, numbers can't proceed a letter, and it can't have any spaces,
or special characters.
"""

def main():
    # Get user input for License Plate
    plate = input("Plate: ")
    # Check Validity of selection
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Length must be between 2 and 6
    if len(s) < 2 or len(s) > 6:
        return False

    # First two chars must be letters
    if s[0].isalpha() is False or s[1].isalpha() is False:
        return False

    # Loop till second to last character
    for i in range(len(s)-1):
        # letter can't follow a number
        if s[i].isdigit() and s[i+1].isalpha():
            return False
        # First number can't be a zero
        elif s[i-1].isalpha() and s[i] == '0':
            return False
        # Check if last number is 0
        elif s[i].isalpha() and s[i+1] == '0':
            return False
        # Only accept letters or numbers. No spaces or special chars
        if s[i].isalnum() is False:
            return False

    return True


if __name__ == "__main__":
    main()
