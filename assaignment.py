# name = "Nikhil Tanwar"
# age = 19
# course = "BTECH"

# print("Name",name)
# print("age",age)
# print("course",course)



# Write a program to print the name, age, and course details of three students.
#  All the details should be stored in separate variables and then print

# name1 = "rahul"
# age1 = "15"
# course1 = "btech"

# name2 = "bihari"
# age2 = "18"
# course2 = "bsc"

# name3 = "mayur"
# age3 = "19"
# course3 = "BBA"

# print("student name :",name1)
# print("age",age1)
# print("course",course1)

# print("student name :",name2)
# print("age",age2)
# print("course",course2)

# print("student name :",name3)
# print("age",age3)
# print("course",course3)

# names = ["mayur","bihari","piyush"]
# ages = [16,17,18]
# courses = ["btech","bca","bsc"]

# for i in range(3):
#     print("student",i+1)
#     print("name",names[i])
#     print("age",ages[i])
#     print("course",courses[i])
#     print()

a=1
b=2

# a = a+b 
# print("sum =",a)

# a = float(input("enter the number"))
# b = float(input("enter the second number"))

# c = a*b
# print("multiply of a and b is",c)

# 5

# ch = input("enter a character: ")
# print("ASCHI value =",ord(ch)) # ord (gives the asii value of character )

# 6th question

# a = int(input("enter the first number "))
# b = int(input("enter the second number"))

# print("sum=",a + b)


# 7th que 
# a = int(input("enter the first number: "))
# b = int(input("enter the second number: "))
# print("the diffrence is =",a - b)

 # que 8

# a = int(input("enter the first number: "))
# b = int(input("enter the second number: "))
# print("the multiplication of  =",a * b)

# que 9

# a = int(input("enter the first number: "))
# b = int(input("enter the second number: "))
# print("the division is =",a / b)


# 10th question\\

# 

# 11th question\\

# a = int(input("enter the first number: "))
# b = int(input("enter the second number: "))
# result = a % b
# print("the reminder is =",result)


# 12th question\\

# a = int(input("enter the number: "))
# b = int(input("enter the power: "))
# result = a ** b
# print("the power value of a is  =",result)


# plant = input("enter plant namee: ")

# if plant == "Spathiphylluon":
#     print("yes - Spathiphyllum is the best plant ever!")

# elif plant == "spathipyllon":
#     print("No, I want a big Spathiphyllum")

# else:
#     print("Spathiphyllum! Not",plant + "!")


# for temp in range(1, 7):
#     print(str(temp)*temp)

                                          # ASSIGNMENT 2 
                                        #   /// QUESTION 1 ///
                                        
# - Write a program that utilizes the concept of conditional execution, takes a string as input, and:
# 1. prints the sentence "Yes - Spathiphyllum is the best plant ever!" to the screen 
# 2. ⁠if the inputted string is "Spathiphyllum" (upper-case)
# prints "No, I want a big Spathiphyllum!" 
# 3. if the inputted string is "spathiphyllum" (lower-case)
# prints "Spathiphyllum! Not [input]!" otherwise. Note: [input] is the string taken as input.

# 1. Accept the floating-point value for income
income = float(input("Enter the annual income in thalers: "))

# Initialize the tax variable
tax = 0.0

# Calculate the tax based on the rules
if income <= 85528:
    # Rule 1: 18% of the income minus 556 thalers and 2 cents
    tax = (income * 0.18) - 556.02
else:
    # Rule 2: 14,839 thalers and 2 cents + 32% of the surplus over 85,528
    surplus = income - 85528
    tax = 14839.02 + (surplus * 0.32)

# Note: If the calculated tax is less than zero, it means no tax at all
if tax < 0:
    tax = 0.0

# 2. Round the calculated tax to full thalers
tax = round(tax)

# Print the final result
print(f"The calculated tax is: {tax} thalers")


