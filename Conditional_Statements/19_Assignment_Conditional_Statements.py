# Get marks for a student and print grade (if < 30, fail, <50 third class, 
# <60 second class, <70 first class, >=70 distinction, =100 then gold medal

a = float(input("Enter Markd of student: ")) # take input from user

if (a<=30): # condition to check the mark range
    
    print ("Student is fail")

elif (a>=30 and a<=50): # condition to check the mark range

    print ("Student got third class") #print

elif (a>=50 and a<=60): # condition to check the mark range

    print ("Student got second class") #print

elif (a>=60 and a<=70): # condition to check the mark range

    print ("Student got first class") #print

elif (a>=70 and a<100): # condition to check the mark range

    print ("Student got distinction") #print

else:
    print ("Student got gold medal") #print