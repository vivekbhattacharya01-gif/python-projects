
# ARITHEMATIC OPERATORS-------------------

#  { + } --  Addition operator (+) is used to add two numbers or concatenate two strings.
#  { - } --  Subtraction operator (-) is used to subtract one number from another. 
#  { * } --  Multiplication operator (*) is used to multiply two numbers or repeat a string a specified number of times. 
#  { / } --  Division operator (/) is used to divide one number by another and returns a float result. 
#  { // } -- Floor division operator (//) is used to divide one number by another and returns the largest integer less than or equal to the result. 
#  { % } -- Modulus operator (%) is used to find the remainder when one number is divided by another. 
#  { ** } -- Exponentiation operator (**) is used to raise a number to the power of another number. 


a = 10
b = 3
c = a + b       # c will be 13
d = a - b       # d will be 7
print (c)
print (d)
# --------------------------------------------------------------------------------------------------------

# ASSIGNMENT OPERATORS-------------------

#  { = } -- Assignment operator (=) is used to assign a value to a variable.
#  { += } -- Add and assign operator (+=) is used to add a value to a variable and assign the result back to the variable.
#  { -= } -- Subtract and assign operator (-=) is used to subtract a value from a variable and assign the result back to the variable.
#  { *= } -- Multiply and assign operator (*=) is used to multiply a variable by a value and assign the result back to the variable.
#  { /= } -- Divide and assign operator (/=) is used to divide a variable       

#  by a value and assign the result back to the variable.

#  { //= } -- Floor divide and assign operator (//=) is used to floor divide a variable by a value and assign the result back to the variable.
#  { %= } -- Modulus and assign operator (%=) is used to find the modulus of a variable by a value and assign the result back to the variable.
#  { **= } -- Exponentiation and assign operator (**=) is used to raise a variable to the power of a value and assign the result back to the variable.    

a = 8 - 2
print (a)       # a will be 6

b = 5
b += 3          # Increment the value of b by 3 and assign the result back to b
print (b)       # b will be 8 (5 + 3)

b -= 2          # Decrement the value of b by 2 and assign the result back to b
print (b)       # b will be 6 (8 - 2)

b *= 4          # Multiply the value of b by 4 and assign the result back to b
print (b)       # b will be 24 (6 * 4)

b /= 6          # Divide the value of b by 6 and assign the result back to b
print (b)       # b will be 4.0 (24 / 6)

# --------------------------------------------------------------------------------------------------------

# COMPARISON OPERATORS-------------------

#  { == } -- Equal to operator (==) is used to compare two values for equality and returns True if they are equal, otherwise returns False.
#  { != } -- Not equal to operator (!=) is used to compare two values for inequality and returns True if they are not equal, otherwise returns False.
#  { > } -- Greater than operator (>) is used to compare two values and returns True if the left value is greater than the right value, otherwise returns False.
#  { < } -- Less than operator (<) is used to compare two values and returns True if the left value is less than the right value, otherwise returns False.
#  { >= } -- Greater than or equal to operator (>=) is used to compare two values and returns True if the left value is greater than or equal to the right value, otherwise returns False.
#  { <= } -- Less than or equal to operator (<=) is used to compare two values and returns True if the left value is less than or equal to the right value, otherwise returns False.    

#  [IN COMPARISON OPERATORS, THE RESULT IS ALWAYS A BOOLEAN VALUE (True or False) BASED ON THE COMPARISON OF THE TWO VALUES.] 

d = 10 > 43
print (d)       # D will be False because 10 is not greater than 43.

e = 5 <= 5 
print (e)       # e will be True because 5 is less than or equal to 5.

f = 7 != 7      # { != } -- Not equal to operator
print (f)       # f will be False because 7 is equal to 7.



#                           |  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -|  
#                           |  NOTE: The assignment operator (=) and the comparison operator (==) are different.|
#                           |     {=} - It is used  for assigning the values.                                   |
#                           |     {==} - It is used for comparing the values.                                   |
#                           |  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -|


# ---------------------------------------------------------------------------------------------------------

# LOGICAL OPERATORS-------------------

#  { and } -- Logical AND operator (and) is used to combine two boolean expressions and returns True if both expressions are True, otherwise returns False.
#  { or } -- Logical OR operator (or) is used to combine two boolean expressions and returns True if at least one of the expressions is True, otherwise returns False.
#  { not } -- Logical NOT operator (not) is used to negate a boolean expression and returns True if the expression is False, and returns False if the expression is True.   


                                                      # [OR]

g = True and False   #For and operator, if both expressions are True, then the result will be True.
print (g)            # g will be False because both expressions are not True.

                                                      # [AND]

h = True or False    # For or operator, if at least one of the expressions is True, then the result will be True.  
print (h)            # h will be True because at least one of the expressions is True.

                                                      # [NOT]

i = not True
print (i)       # i will be False because the expression is negated.

# NOT - The not operator only operates on a single operand and gives the value , which is either True or False.
# meaning it turns 'true' into 'False' and 'False' into 'True'.

print(not(False))
print(not(True))

