# Write a python program to take number from the user and check if the number is palidrome or not

number=(input("Enter number to check the palidrome: "))

intNum=int(number)

newNum=int(0)
for a in range(len(number)):
    newNum=newNum*10+(intNum%10)
    intNum=intNum//10

if newNum == int(number):
    print(f"Your Number {number} is palidrome")
else:
    print(f"Your Number {number} is not a palidrome")