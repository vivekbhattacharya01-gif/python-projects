
#                                      STRINGS IN PYTHON........

# A string is a sequence of characters enclosed in single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).
# It is a datatype in python that is used to represent text. 
# A String is Immutable, which means that once a string is created, it cannot be modified.

name = "Vivek Bhattacharya"   # A string variable named 'name' is assigned the value "Vivek Bhattacharya".
print(name)    # Output: Vivek Bhattacharya, because the value of the variable 'name' is "Vivek Bhattacharya".


# STRING SLICING IN PYTHON.......

# A String starts from index 0 and ends at index n-1, where n is the length of the string.
# For example, in the string "Hello, World!", the character 'H' is at index 0,
#            'e' is at index 1, 'l' is at index 2, and so on. The character '!' is at index 12 (length of the string - 1).

#  A String can be sliced using the slicing operator [ ] in python. The syntax for slicing a string is as follows:
# string[start:stop:step]
s = "Hello, World!"   # A string variable named 's' is assigned the value "Hello, World!".
print(s[0:5])   # Output: Hello, because the slice s[0:5] returns the substring from index 0 to index 4 (5-1) of the string 's'.
print(s[7:])    # Output: World!, because the slice s[7:] returns the substring from index 7 to the end of the string 's'.
print(s[:5])    # Output: Hello, because the slice s[:5] returns the substring from the beginning of the string 's' to index 4 (5-1).
print(s[::2])   # Output: Hlo ol!, because the slice s[::2] returns every second character of the string 's' starting from index 0.

# To find the length of a string, we can use the len() function in python. The syntax is as follows:
a = "Hello, World!"   # A string variable named 'a' is assigned the value "Hello, World!".
print(len(a))   # Output: 13, because the length of the string 'a' is 13 characters (including spaces and punctuation).