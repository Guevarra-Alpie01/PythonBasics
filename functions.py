#we will create a function that will check if the number is odd or even

def checknum(x):
    if x % 2 ==0:
        return("even")
    else:
        return("odd")

print(checknum(2))
print(checknum(3))


#Now we will do a default arguments in declaring functions

print("default arguments in function")

def MyFunction(a,b = 100):      #there is a defult value for the parameter b,while a is empty
    print(a,b)
    


MyFunction(20)                  #add a value for an empty variable a

#Next is the keyword arguments where parameters are set by name so that values dont have orders 

print()
print("keyword arguments")

def student(id,name):               #set name parameters 
    print(id,name)

student(10,"Alpie Guevarra")        #set the value of id into integer and the name to string     


