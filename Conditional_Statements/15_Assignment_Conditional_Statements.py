# get 3 numbers from the user and find maximum

num1 = int(input("enter 1st no: "))  # take input from user

num2 = int(input("enter 2nd no: ")) # take input from user

num3 = int(input("enter 3rd no: ")) # take input from user

if(num1 > num2 and num1 > num3): # condition to check number

    print("1st no is max") # print 

elif(num2 > num1 and num2 > num3): # condition to check number

    print("2nd no is max") # print 

else:
    print("3rd no is max") # print 

