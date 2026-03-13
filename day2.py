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



#create another sample of  class 


class House:
    def __init__(self, door, window):
        self.door = door
        self.window = window

blueprint = House("wooden door", "glass window")
builder = House("panday" , "engineer")

print(blueprint.door)
print(blueprint.window)
print(f"builder of door {builder.door}")
print(f" builder of window:{builder.window}")


                                    #Conditional statament 
                                    #nested if statement 

breed1 = 40
breed2 = 25

if breed1 >=35:                     #check if the breed1 is greater or equal to 35 return true if that condition is met
    print("breed is sufficient!")
    #run if the condition above is met
    if breed2 >30:    #execute if breed 2 is above 30
        print("breed 2 is higher!!")

    elif breed2 ==30:   #execute if breed2 is equal to 30
        print("breed 2 is equal to 30")

    else:   #if no condition is met then execute this 
        print ("breed 2 is lower to 30")   
else:                               #execute if breed 1 is less than 35
    print("invalid breed!!")


"""Check Even or Odd
Input: A number from the user
Output: "Even" or "Odd"
Concepts: if, else, % operator
"""

input = int(input("Enter one number:"))

if input % 2:
    print ("odd number")

else:
    print("even number")