#Task 1
a=int(input("Enter a Number: "))
if a%2==0:
    print(f"{a} is a even number")
else:
    print(f"{a} is a odd number")

#Task 2
s=0
for i in range(1,51):
    s=s+i
print("Sum of 1-50 number is: ",s)