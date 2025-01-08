
#Write a generator function that generates the first 10 even numbers
'''
def even_numbers():
    for i in range(10):
        print(i*2)

for even in even_numbers():
    print(even)
'''

#Write a Python program that uses a custom iterator to iterate over a list of integers
def list_iterator(data):
    for item in data:
        return item
numbers = [1, 2, 3, 4, 5]

for num in list_iterator(numbers):
    print(num)
