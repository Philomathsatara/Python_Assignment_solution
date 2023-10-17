# Ask user to enter number if number is in 1s then print one, if number is in 10s 
# then print ten if number is in 100s then print hundred if number is in 1000s then print thousand. 
# (try to implement this using if-elif-else)

n = int(input("Enter a number: ")) # take input from user

if(n <= 9 ): # condition to check number

    print("one's")  # print 

elif(n <= 99): # condition to check number

    print("ten's")  # print 

elif(n <= 999): # condition to check number

    print("hundred's")  # print 

elif(n <= 9999): # condition to check number

    print("thousand's")  # print 
    
else:
    print("greater than ten thousand")  # print 





