# Get three sides of a triangle from user and check if that is a valid triangle

a = int(input("enter 1st side of triangle: ")) # take input from user

b = int(input("enter 2nd ide of triangle: ")) # take input from user

c = int(input("enter 3rd ide of triangle: "))# take input from user

if (a + b >= c and a + c >= b and b + c >= a): # condition to check the triangle validity

    print ("This is valid triangle") # print

else:
    print("This is not valid triangle")  # print