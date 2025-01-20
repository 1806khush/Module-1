#Write a Python program to apply the map() function to square a list of numbers

def double(n):
    return n*2
n  = [1,3,4,2,6]
result = map(double,n)
print(list(result))

#Write a Python program that uses reduce() to find the product of a list of numbers.

def double(n):
    return n%2==0
n  = [1,3,4,2,6]
result = filter(double,n)
print(list(result))

#Write a Python program that filters out even numbers using the filter() function.

# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))
