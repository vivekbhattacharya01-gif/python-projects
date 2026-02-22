
#                                  ---- TYPE FUNCTIONS IN PYTHON ----



# 1.   type() function is used to find the data type of a given variable in python.
# 2.   type() function is used to determine the type of a variable or a value in Python. 
# 3.   It returns the type of the object passed as an argument.

a = 23
print(type(a))     # Output: <class 'int'>, because a is an integer.

                                        #    OR

a = 34
t = type(a)
print(t)           # Output: <class 'int'>, because a is an integer.

b = 3.14
print(type(b))     # Output: <class 'float'>, because b is a floating-point number.

c= "yooo"
print(type(c))     # Output: <class 'str'>, because c is a string.



# NOTE: The type() function can also be used to create new types or classes in Python.
#     For example, A number can be converted into a string and vice versa using the type() function.

# There are many functions in Python that can be used to convert one data type to another. 

# str(31) => '31'     # Converts the integer 31 to a string '31' using the str() function.
# int('31') => 31     # Converts the string '31' to an integer 31 using the int() function.
# float(3) => 3.0     # Converts the integer 3 to a floating-point number 3.0 using the float() function.

a = " 31.2"
t = float(a)  
c = type(t)     # Converts the string ' 31.2' to a floating-point number 31.2 using the float() function.
print(c)           # Output: <class 'float'>, because t is a floating-point number.