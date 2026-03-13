# loop that stops till it reach 20
course = 100      #  A list of courses

for check in range(course):
    if check <= 20:
        print(check)
        continue
    else:
        print("reach 20")
        break


#loop through tuples
tups = ("app", "hap", "dap" , "lap")    

for index in range(len(tups)):
    print(index)


#nested loops 

print("this is a nested loops ")



for a in range(10):
    for j in range( 2 * a + 1):
        print("*",end='')
    print()
        
print()
print("christmas tree")


#created a Christmastree
christmastree = 20

for j in range(christmastree):
    for a in range(christmastree -j -1):
        print(" " ,end='')

    for i in range( 2 * j + 1):
        print("*",end='')

    print()

     
truck=5
for truck in range(5):
    for x in range(christmastree -1):
        print(" ", end='')
    print("|")
print() 
