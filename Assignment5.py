
#Task 1
name=input("please Enter Student's name:")
dict1={'John':36,'Alice':85,'Sam':56}

a=name in dict1
if a==True:

    print(f'{name} has {dict1.get(name)} marks')
else:
    print('Student not found')


#Task 2
List1=[1,2,3,4,5,6,7,8,9,10]
s=List1[0:5]
print('Complete List:',List1)
print('Extracted first five:',s)
print('Reversed Extracted five',s[::-1])