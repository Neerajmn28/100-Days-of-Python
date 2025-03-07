# Args and Kargs in Python
'In Python, args and kwargs are used to handle variable-length arguments in functions'
 
# args (Non-Keyword Arguments)
 
'args (Non-Keyword Arguments)'
'args allows a function to accept any number of positional arguments.'
'Inside the function, args is treated as a tuple'

('Arguments with Default Values')

def my_function(a = 1, b = 2, c = 3): # The default value
    


my_function(b = 5) # I can change the default value


('Unlimited Arguments')

'Unlimited arguments means a function that can take any number of arguments'

def add(*args):
    for item in args:
        print(item)
    
def add(*args):
    sum = 0
    for item in args:
        sum += item
    return sum
    

add(3,5,6,8,2,3,4,2,3,4)

# kwargs (Keyword Arguments)
'kwargs allows a function to accept any number of keyword arguments (name-value pairs).'
'Inside the function, kwargs is treated as a dictionary.'


def calculate(**kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)
        
calculate(key = 'X', value = 200)


def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)
    
    
calculate(2, add = 3, multiply = 5)
    