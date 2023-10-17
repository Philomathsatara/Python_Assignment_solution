# Get a number from user, write a program to check if number is prime number

n = int(input("Enter a number: "))
for i in range(2,n+1):
    if (n % i) == 0:    
        print(n, "is not a prime number")
        break
    else:
         print(n, "is a prime number")
         break