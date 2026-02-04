# QUESTION - 4
# WRITE A PYTHON PROGRAM TO PRINT THE CONTENTS OF A DIRECTORY USING OS MODULE. SEARCH  ONLINE FOR THE FUNCTION WHICH DOES THAT.  

import os

# Ask user for the directory path
path = input("Enter directory path: ")

try:
    # Get the list of entries in the directory
    contents = os.listdir(path)

    print(f"Contents of '{path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print("Directory not found!")
except PermissionError:
    print("You don't have permission to access this directory!")


    # solved using GHATGPT 
