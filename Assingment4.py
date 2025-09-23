#Task 1
import os
a = input('file name:')
try:
    with open(a, 'r+') as file1:
        file1.write('This a a sample text file\nIt has multiple lines')

    with open(a, 'r') as file1:
        r = file1.read()
    print(r)

except FileNotFoundError:
    print(f"File '{a}' not found")


#Task 2
b=input("Enter text to write to the file:")
print("Data sucessfully written in 'output.txt' file")
c=input("Enter additional text to append to the file:")
with open('output.txt','r+') as file1:
    file1.truncate()
    file1.write(f'{b} ')
with open('output.txt','a') as file1:
    file1.write(f'{c}')
with open('output.txt','r') as file1:
    R=file1.read()
    print(R)