#example-1-Write a Python program to find greater and less than a number using

num1 = 10
num2 = 20

if num1 > num2:
    print(f"{num1} is greater than {num2}")
else:
    print(f"{num1} is less than {num2}")

#example-2-Write a Python program to check if a number is prime using if_else.
num = 29
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

#example-3-Write a Python program to calculate grades based on percentage using
percentage = 85

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is {grade}")

#example-4-Write a Python program to check if a person is eligible to donate blood

age = 25
weight = 60

if age >= 18:
    if weight >= 50:
        print("Eligible to donate blood")
    else:
        print("Not eligible due to insufficient weight")
else:
    print("Not eligible due to age")
