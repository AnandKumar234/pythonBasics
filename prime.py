num = int(input("enter the number:"))
check = True
for value in range (2,num):
    if(num%value == 0):
        check = False
        break

