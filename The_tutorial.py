#Putting the # in front of an item is comments.
#This doesn't do anything to code.
#Why put comments? To let others know what you are making of course!

#This program will take an input and multiply it by 2.
#print prints a message. The \n is a return character.
#It puts stuff on the next line.
print("This prints the message I want to give\n")

#this takes in an input and stores it into the variable on the left hand side.
#example
name = input("Enter the student's name:")
#now lets store the student's major in a container known as major
major = input("Enter the student's major:")
#now we can create a message with the data to make an automated message!
print("Welcome ", name, "\n")
print("Your major is :", major)

#So why is programming so powerful?
#Because you can automate logical decisions.
#Think of any job that has a logical decision that you have to make a decision.

#This is where the automation of logical work happens
#In python TABS ARE EVERYTHING
#So... If you make an if statement, everything that happens if that circumstance is met
#Is done one tab over.
#For example
#if is the first condition
#elif means else if, for other conditions
#else means for everything else.

#if(condition):
#   what happens during condition. This is tabbed on purpose.
#elif(condition):
#   what happens if the else if condition is met
#else:
#   what happens if anything else isn't made.


#Here is a GPA Calculator for a grade.
print("Make a choice from the following \n")
print("Convert Grade to GPA\n")
print("Type one of the following A, A-, B+, B, B-, C+, C, C-, D+,D, D-, F, \n")
choice = input("Type the grade here:")

if(choice == "A"):
    print("4.0")
elif(choice == "A-"):
    print("3.667")
elif(choice == "B+"):
    print("3.333")
elif(choice == "B"):
    print("3.0")
elif(choice == "B-"):
    print("2.667")
elif(choice == "C+"):
    print("2.333")
elif(choice == "C"):
    print("2.0")
elif(choice == "C-"):
    print("1.667")
elif(choice == "D+"):
    print("1.333")
elif(choice == "D"):
    print("1.0")
elif(choice == "F"):
    print("0.0")
else:
    print("Do not recognize grade")

#But here is something more interesting.
print("Prince is one of the greatest musicians of our time.\n")
prince = input("Enter y for yes, n for no:")
if (prince == "y"):
    print("Of course he is, may purple rain for ever.")
elif(prince =="n"):
    print("WHAT? ARE YOU INSANE! Go purify yourself in the waters of lake Minnetonka!")
else:
    print("You must have meant yes. OBVIOUSLY. The keys slipped.")
    

print("\nEnding program\n")
