#Declare variables and printing it
firstname = "Alpie"
secondname = "Guevarra"
age = 10

print(firstname,secondname,"age:",age)


# Using split to display multiple variables and F-string to displa the inputted value
name1,name2,name3= input("enter 3 names:").split()

print(f"firstname:{name1} secondname:{name2} thirdname:{name3}")

#adding expression on F-string
number1 = 10
number2 = 20

print(f"{number1} + {number2} = {number1 + number2}")

#knowing the type of variable
e=("one", "two", "three")
f={ 1 , 2 , 3}
g=[1, 2, 3]
x ="im string"
y = 20
z = 3.21

print(type(e))
print(type(f))
print(type(g))
print(type(x))
print(type(y))
print(type(z))


#Type casting a variable
number = "10"

cast = int(number) #convert a string into an integer
print(cast)
print(type(cast))


#object reference variable
ref = 120
copy_ref = ref
print(f"this is a copy:{copy_ref}")
print(f"this is the original:{ref}")

ref = "new ref"         #declare new value for ref so the declaration above wil not take effect
print(f"{ref}") 
copy_ref = ref
print(copy_ref)         #copy the new ref


#Logical Operators
a=True
b=True

print(a and b)   #returns true if both statements are true so the result of this is true 
print(a or b)    #returns true if one of the statements is true so the result of this is true
print(not b)    #negate the value of b, the value of b is true so the result is false
print(not a)    #negate the value of a, the value of a is true so the result is false

#assignment operators
a = 10
b = a
print(b)    #print 10

b += a      #operator  b=10 + a=10 = 20
print(b)    #result is 20 

b -= a      #20 - 10
print(b)    # result is 10

b *= a      #now b is 10 multiplied by 10
print(b)    # result is 100


#Operands
a=20
b=20

print(a is b)
print(a is not b)
