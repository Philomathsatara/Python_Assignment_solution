# Ask user to enter name and surname and concatenate name and surname,  
# print name and surname in lower case if name starts with b other wise print name in title case

n = input("Enter name: ") # take input from user

s = input("Enter surname: ") # take input from user

c = n+" "+s  # concatenate name and surname

if  (c[0]=="b"): # condition to check name start with b
    
    print (c.lower())   # print in lower case if name startes with b


elif (c[0]=="B"): # condition to check name start with B

    print (c.lower())  # print in lower case if name startes with B

else:
    print(c.upper())  # print in upper case 

