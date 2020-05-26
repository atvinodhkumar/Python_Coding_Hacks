"""
Script to avoid the blank input from the user. 
"""

def blank_input():
    
    print("Enter input: ")
    user_input = input().strip()
    while user_input == "":
        print("Entered an empty input. Please enter a valid input.")
        user_input = input().strip()
    return user_input

blank_input()
