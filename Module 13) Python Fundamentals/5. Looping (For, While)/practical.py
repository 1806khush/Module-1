#Practical Example 1: Write a Python program to print each fruit in a list using a simple for loop. 

List1 = ['apple', 'banana', 'mango']
for fruit in List1:
    print(fruit)
    
#Practical Example 2: Write a Python program to find the length of each string in List1.

List1 = ['apple', 'banana', 'mango']
for fruit in List1:
    print(len(fruit))
    
#Practical Example 3: Write a Python program to find a specific string in the list using a simple for loop and if condition.

List1 = ['apple', 'banana', 'mango']
target = 'banana'
for fruit in List1:
    if fruit == target:
        print(f"{target} found")
        
#Practical Example 4: Print this pattern using nested for loop:

for i in range(1, 6):
    print('*' * i)
