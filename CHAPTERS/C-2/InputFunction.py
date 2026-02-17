
                                        #   Input Function
# This function allows the user to take input from the keyboard as a string. The syntax is as follows :

a = input("enter a  number : ")
b = input("enter  a number : ")
print(a + b)

# the above code will concatenate the two numbers as they are treated as strings. To perform addition, we need to convert them to integers.
# So , 

a = int(input("enter a number : "))
b = int(input("enter a number : "))
print ("sum is",a + b)

# NOTE : It is important to note that output of input is always a string (even if a number is entered.)