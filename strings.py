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

# with open("data.txt","r") as file:
#     data=file.read()
# print(data)

# with open('students.txt','w') as f:
#     f.write('Rahul Sharma,85,Bhopal\n')
#     f.write('Priya Verma,92,indore\n')
#     f.write('Amit Kumar,90,Jabalpur\n')

# with open('students.txt','a') as f:
#     f.write('Sneha Joshi,88,Bhopal\n')

# with open('students.txt','r') as f:
#     content = f.read()
# print(content)

# with open('students.txt','r') as f:
#     for line in f:
#         name,marks,city=line.strip().split(',')
#         print(f'{name:<15}|{marks:>5}|{city}')
#         print("-----------")

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

# # 1. Create and write data to the CSV file
# CLI = [
#     ['name', 'age', 'maths', 'physics', 'chemistry'],
#     ['khilbil', '16', '65', '74', '78'],
#     ['Bihari', '19', '78', '74', '94'],
#     ['piyush', '22', '43', '99', '99']
# ]

# with open('CLI.csv', 'w', newline="") as f:
#     csv.writer(f).writerows(CLI)

# print("--- Displaying All Students ---")

# with open('CLI.csv', 'r') as f:
    
#     reader = csv.DictReader(f)
    
#     for row in reader:
        
#         print(f"Name: {row['name']} | Age: {row['age']} | Maths: {row['maths']} | Physics: {row['physics']} | Chemistry: {row['chemistry']}")

import numpy as np


# arr1d = np.array([[1,2,3,4,5]])
# arr2d = np.array([[85,90,70],[72,88,23],[91,76,82]])


# print(arr2d.shape)
# print(arr2d.dtype)
# print(arr2d.ndim)


# zeros = np.zeros((3,4))
# print(zeros)

# ones = np.ones((2,5))
# print(ones)
# rng = np.arange(0,50,10)
# print(rng)

# lin = np.linspace(0,1,11)
# print(lin)

# random = np.random.randint(40,100,(5,3))
# print(random)

# arr = np.array([10,20,30,40,68])


# print(arr * 2)
# print(arr + 5)
# print(arr ** 2)


# marks_2d = np.array([[10,20,30],[30,40,50],[60,70,70]])

# print(np.mean(marks_2d))

# print(np.mean(marks_2d, axis=1))

# print(np.mean(marks_2d, axis=0))

# print(np.max(marks_2d))

# print(np.std(marks_2d))


arr = np.array([10,50,78,69,84.58,99,84])
print(arr[arr>70])

# panda ji

import pandas as pd
# print(pd.__version__)

data = {
    'Name': ['pari','teshu','harsh','kunal','mayur'],
    'Age':  [20, 21, 23, 24, 40],
    'Marks': [90,59,80,98,77],
    'city': ['Kashrawad','Patna','bihar','indore','pune'],

}
df = pd.DataFrame(data)
print(df)
print(df.shape)
print(df.head(3))
print(df.dtypes)
print(df.describe())