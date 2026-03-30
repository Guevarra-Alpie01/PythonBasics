global num1
global num2
global operate


def calculate(solusyon):
    print(input(num1))   
    print(input(operate))
    print(input(num2))
    if operate == '+':
        return num1 + num2
    elif operate == '-':
        return num1-num2
    elif operate == 'x':
        return num1*num2
    elif operate == '/':
        return num1/num2
    else: 
        print("invalid input")
            

calculate(solusyon)


