#we will create a function that will check if the number is odd or even

def checknum(x):
    if x % 2 ==0:
        return("even")
    else:
        return("odd")

print(checknum(2))
print(checknum(3))
