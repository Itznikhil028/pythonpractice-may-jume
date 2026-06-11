# spilit and join

# Split and Join
# csv = 'Rahul,22,Bhopal,Engineer'
# parts = csv.split(',')                 
# print(parts)
# print(parts[0])
# rejoined = ' | '.join(parts)

# # Check content
# print('hello123'.isalnum())
# print('12345'.isdigit())               
# print('Python'.isalpha())              
# print(' '.isspace())                   
# # Start/end check
# email = 'student@gmail.com'
# print(email.endswith('.com'))
# print(email.startswith('stu'))         

# name, marks, rank = 'Anita', 92.567, 3


# print(f'Hello, {name}!')


# print(f'Marks: {marks:.2f}')          
# print(f'Marks: {marks:.0f}')          
# print(f'Count: {1000000:,}')          
# # Padding and alignment
# print(f'{name:<15}|{marks:>8.2f}|Rank:{rank}')  # left/right align
# # Anita          |   92.57|Rank:3

# # Expressions inside {}
# price, gst = 500, 0.18
# print(f'Price:Rs.{price} | GST:Rs.{price*gst:.2f} | Total:Rs.{price*(1+gst):.2f}')


# name = "Hello how are you doing today0"


# Vowels = "aeiouAEIOU"
# Vovels_count = sum(1 for char in name if char in Vowels)
# print(f"vowels count: {Vovels_count} ")

# start_idx = name.find("you")
# if start_idx != -1:
#     print(name[start_idx:start_idx+3])

# print(name[::-1])

# non_palin, palin = "abcdef", "axttxa"


# def check_palindrome(s):
#     return s == s[::-1]

# print(f"Is '{non_palin}' a palindrome?: {check_palindrome(non_palin)}")
# print(f"Is '{palin}' a palindrome?: {check_palindrome(palin)}")


# import csv

# records = [
#     ['name','marks','city','grade'],
#     ['rahul','85','indore','B'],
#     ['bihari','86','bihar','A'],
#     ['mayur','64','mumbai','A']
# ]
# with open('students.csv','w',newline="") as f:
#     csv.writer(f).writerows(records)

# with open('students.csv','r') as f:
#     for row in csv.DictReader(f):
#         print(f'{row["name"]}: {row["marks"]} marks ({row["city"]})')

# import csv

# CLI = [
#     ['name','age','maths','physics','chemistry'],
#     ['khilbil','16','65','74','78'],
#     ['Bihari','19','78','74','94'],
#     ['piyush','22','43','99','99']
# ]
# with open('CLI.csv','w',newline="") as f:
#     csv.writer(f).writerows(CLI)

# name = input("enter the student name: ")

# found = False

# with open('CSI.csv','r') as f:
#     for row in csv.DictReader(f):
#         if row["name"] == name:
#             print(f'Found {name}')
#             print(f'{row["name"]}: {row["age"]} age (row{"maths"})')



import numpy as np


arr1d = np.array([[1,2,3,4,5]])
arr2d = np.array([[85,90,70],[72,88,23],[91,76,82]])


print(arr2d.shape)
print(arr2d.dtype)
print(arr2d.ndim)