# Lambda functions are small anonymous functions defined using the lmbda functions keyword they can have any number or argument but only one expression.

addition = lambda a,b : a+b
type(addition)

even1 = lambda num : num % 2 == 0
even1(24)

addition1 = lambda x,y,z : x+y+z
addition1(100,51,60)


numbers = [1,2,4,5,7]
list(map(lambda x:x**2, numbers))

num1 = [1,2,3]
num2 = [4,5,6]

added_numbers = list(map(lambda x,y : x+y, num1, num2))
print(added_numbers)

# Map to convert a list of strings to integers

str_numbers = ['1','3','5','6','7']

int_num = list(map(int,str_numbers))
print(int_num) 

# Capitalizing

words = ['apple','banana']

upper_word = list(map(str.upper, words))
print(upper_word)

def get_name(person):
    return person['name']

people = [
    {'name':'Neeraj','age':24},
    {'name':'Sweetu','age':19}
]

list(map(get_name,people))

# Filter Function
# The filter function constructs an iterator from elements of an iterable for which a function returns true. It is used to filter out items from a list

def even(num):
    if num %2 == 0:
        return True
even(24)


lst = [1,2,3,4,5,6,7,8,8,9,10,12]
list(filter(even,lst)) # Applies a filter and returns all the even numbers

# filter with a lambda function
numbers = [1,2,3,4,5,6,7,8]
greater_than_five = list(filter(lambda x:x>5, numbers))
print(greater_than_five)

# filter with a lambda function and multiple conditions
numbers = [1,2,3,4,5,6,6,7,8]
even_and_greater_than_five = list(filter(lambda x:x>5 and x%2 == 0, numbers))
print(even_and_greater_than_five)

# Apply a filter to check if the age is greater than 25 in dict

people = [
    {'name':'Neeraj','age':24},
    {'name':'Nandana','age':28}
]

def age_greater_than_25(person):
    return person['age'] > 25

list(filter(age_greater_than_25, people))
