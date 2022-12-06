
#1.	Accept a char input from the user and display it on the console.
n1= str(input("enter a name"))
print(n1)

#2.	Accept two inputs from the user and output its sum.
n1=int(input("enter n1"))
n2=float(input("enter n2"))
sum=n1+n2
print(sum)

#3.	Write a program to find the simple interest.
p=int(input("enter principal amount"))
r=float(input("enter interest rate"))
y=float(input("enter years"))
si=(p*r*y)/100
print(si)

# 4.	Write a program to check whether a student has passed or failed in a subject after he or she enters their mark (pass mark for a subject is 50 out of 100).
mark=float(input("enter mark"))
if mark>=50:
    print("passed")
else:
    print("failed")
    
#Write a program to show the grade obtained by a student after he/she enters their total mark percentage.
mark=float(input("enter mark"))
if mark>=90:
    print("A")
elif mark>=80 and mark<=89:
    print("B")
elif mark>=70 and mark<=79:
    print("C")
elif mark>=60 and mark<=69:
    print("D")
elif mark>=50 and mark<=59:
    print("E")    
else:
    print("failed")
    
#6.	Using the ‘switch case’ write a program to accept an input number from the user and output the day as follows. 
number=int(input("enter number"))
if mark>=90:
    print("A")
elif mark>=80 and mark<=89:
    print("B")
elif mark>=70 and mark<=79:
    print("C")
elif mark>=60 and mark<=69:
    print("D")
elif mark>=50 and mark<=59:
    print("E")    
else:
    print("failed")    



