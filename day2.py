""""

1. Arithmetic Operators

Ask the user for two numbers and print:

sum

difference

product

quotient

remainder

Ask for the radius of a circle and compute the area.

Ask for a number and print:

its square

its cube

Convert minutes to hours and remaining minutes.

Example:
130 minutes → 2 hours 10 minutes

"""

num1 = int(input("Enter first number:"))
num2 = int(input("second number:"))

total = num1 + num2
print( total )



# creating an object using init function

class Color:    #create a class 
    def __init__(self, color1, color2):     # create a constructor with two parameters the color1 and color2
        self.color1 = color1                #declare the instance variable color1 and assign the value of the parameter color1 to it
        self.color2 = color2

new = Color("pink", "rainbow")              #create an object of the class and pass the value for the parameters

print(f"first color: {new.color1}")         #print the value of the instance variable color1 using the object new
print(f"second color: {new.color2}")        #print the value of the instance variable color2 using the object new