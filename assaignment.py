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



# tax question
# 1. Accept the floating-point value for income
# income = float(input("Enter the annual income in thalers: "))

# # Initialize the tax variable
# tax = 0.0

# # Calculate the tax based on the rules
# if income <= 85528:
#     # Rule 1: 18% of the income minus 556 thalers and 2 cents
#     tax = (income * 0.18) - 556.02
# else:
#     # Rule 2: 14,839 thalers and 2 cents + 32% of the surplus over 85,528
#     surplus = income - 85528
#     tax = 14839.02 + (surplus * 0.32)

# # Note: If the calculated tax is less than zero, it means no tax at all
# if tax < 0:
#     tax = 0.0

# # 2. Round the calculated tax to full thalers
# tax = round(tax)

# # Print the final result
# print(f"The calculated tax is: {tax} thalers")




# # Read the year from the user
# year = int(input("Enter a year: "))

# # Check if the year falls into the Gregorian era
# if year < 1582:
#     print("Not within the Gregorian calendar period.")
# else:
#     # Rule 1: If it's not divisible by 4, it's a common year
#     if year % 4 != 0:
#         print("Common year")
#     # Rule 2: If it is divisible by 4 but not by 100, it's a leap year
#     elif year % 100 != 0:
#         print("Leap year")
#     # Rule 3: If it's divisible by 100 but not by 400, it's a common year
#     elif year % 400 != 0:
#         print("Common year")
#     # Rule 4: Otherwise (divisible by 400), it's a leap year
#     else:
#         print("Leap year")




# import time

# # Loop from 1 to 5
# for i in range(1, 6):
#     print(f"{i} Mississippi")
#     time.sleep(1)  # Pause for 1 second to match real clock-time

# # The final message after the loop finishes
# print("Ready or not, here I come!")



# You must design the (ugly) vowel eater! Write a program that uses:
# 1. a for loop;
# 2. the concept of conditional execution (if-elif-else)
# 3. the continue statement.
# Your program must:
# 1. ask the user to enter a word
# 2. use user_word = user_word.upper() to convert the word entered by the user to upper case; we'll talk about string methods and the upper() method very soon - don't worry;
# 3. use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
# 4. ⁠assign the uneaten letters to the word_without_vowels variable and print the variable to the screen.

# word = input("enter the word")

# word = word.upper()

# word_without_vowels = ""

# for letter in word:
#     if letter == "A":
#         continue
#     elif letter == "E":
#         continue
#     elif letter == "I":
#         continue
#     elif letter == "O":
#         continue
#     elif letter == "U":
#         continue
#     else:
#         # 4. Assign the uneaten letters to the variable
#         word_without_vowels += letter

# # 4. Print the final variable to the screen
# print(word_without_vowels)


# # Read the total number of blocks from the user
# blocks = int(input("Enter the number of blocks: "))

# height = 0
# current_layer_requirement = 1

# # Keep building as long as we have enough blocks for the next layer
# while blocks >= current_layer_requirement:
#     blocks -= current_layer_requirement  # Use up the blocks for this layer
#     height += 1                          # The layer is successfully built!
#     current_layer_requirement += 1       # The next layer will need 1 more block

# # Output the final height of the completed pyramid
# print("The height of the pyramid:", height)






# # Read a natural number from the user
# c0 = int(input("Enter a non-zero, non-negative integer: "))

# # Ensure the input is valid based on the rules (greater than 0)
# if c0 <= 0:
#     print("Please enter a valid natural number (greater than 0).")
# else:
#     # Variable to keep track of the total steps
#     steps = 0

#     # Execute the steps as long as c0 remains different from 1
#     while c0 != 1:
#         # Rule 2: If it's even
#         if c0 % 2 == 0:
#             c0 = c0 // 2  # Using integer division to keep it as an integer
#         # Rule 3: If it's odd
#         else:
#             c0 = 3 * c0 + 1
        
#         # Print each intermediate value
#         print(c0)
        
#         # Increment the step counter
#         steps += 1

#     # Output the total number of steps taken
#     print("Total steps executed:", steps)






# Initial list inside the hat
hat_list = [1, 2, 3, 4, 5]

# Step 1: Write a line of code that prints the length of the existing list.
print("Length of the list:", len(hat_list))

# Step 3: Write a line of code that prompts the user to replace the middle number.
# (We do Step 3 before Step 2 so that the list still has 5 elements and a clear middle index of 2)
hat_list[2] = int(input("Enter an integer to replace the middle number: "))

# Step 2: Write a line of code that removes the last element from the list.
del hat_list[-1]

# Let's print the final list to see the changes
print("Final list:", hat_list)






# # Step 1: Create an empty list named beatles
# beatles = []
# print("Step 1 (Empty list):", beatles)

# # Step 2: Use the append() method to add John, Paul, and George
# beatles.append("John Lennon")
# beatles.append("Paul McCartney")
# beatles.append("George Harrison")
# print("Step 2 (Core members added):", beatles)

# # Step 3: Use a for loop and append() to prompt the user to add Stu and Pete
# print("\n--- Step 3: Adding early members ---")
# for i in range(2):
#     new_member = input("Enter a band member to add (Stu Sutcliffe / Pete Best): ")
#     beatles.append(new_member)
# print("Step 3 (With Stu and Pete):", beatles)

# # Step 4: Use the del instruction to remove Stu Sutcliffe and Pete Best
# # Note: Since Stu and Pete are at the end of the list (indices 3 and 4), 
# # removing index 3 shifts the next element down to index 3.
# del beatles[3]  # Removes Stu Sutcliffe
# del beatles[3]  # Removes Pete Best (who shifted to index 3)
# print("\nStep 4 (Stu and Pete removed):", beatles)

# # Step 5: Use the insert() method to add Ringo Starr to the beginning of the list
# beatles.insert(0, "Ringo Starr")
# print("Step 5 (Final legendary line-up):", beatles)




pattern_list = []

for i in range (1, 51):
    if i % 3 == 0 and i % 5 == 0:
        pattern_list.append("FizzBuzz")
    elif i % 3 == 0:
        pattern_list.append("Fizz")
    elif i % 5 == 0:
        pattern_list.append("Buzz")
    else:
        pattern_list.append(i)

print(pattern_list)



input_string = "MindCoders"

# Convert string to lowercase to handle both 's' and 'S' uniformly
lower_string = input_string.lower()

# Count the occurrences of 's'
s_count = lower_string.count('s')

print(f"Output: {s_count}")


def count_digits(input_string):
    digit_count = 0
    for char in input_string:
        if char.isdigit():
            digit_count += 1
    return digit_count

# Test Case 1
string1 = "MindCoders password2 is : 1234"
print(f"Total number of Digits = {count_digits(string1)}")

# Test Case 2
string2 = "U r a a n S 0 f t s k i l l 1 s 1234"
print(f"Total number of Digits = {count_digits(string2)}")



