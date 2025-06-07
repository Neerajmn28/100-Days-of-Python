# A FUNCTION TO CONVERT THE TEMPERATURE

def convert_temperature(temp,unit):
    if unit == 'C':
        return temp * 9/5 + 32
    elif unit == 'F':
        return (temp - 32) * 5/9 
    else:
        return None
    
# A FUNCTION TO CHECK IF THE PASSWORD USER ENTERED IS STRONG OR NOT  
convert_temperature(20,'F')


def is_strong_password(password):
    '''This function checks if the password is strong or not'''
    if len(password) < 8:
        return False
    if not any (char.isdigit() for char in password):
        return False
    if not any (char.lower() for char in password):
        return False
    if not any (char.upper() for char in password):
        return False
    if not any (char in '@#$' for char in password):
        return False
 
 
 
# A FUNCTION TO CALCULATE THE INVENTORY   
def calculate_total_cost(cart):
    total_cost = 0
    for item in cart:
        total_cost += item['price'] * item['quantity']
    return total_cost

cart = [
    {'name':'Apple','price':0.5,'quantity':4},
    {'name':'Banana','price':0.3,'quantity':6},
    {'name':'Ornage','price':0.7,'quantity':3}
]  


total_cost = calculate_total_cost(cart)
print(total_cost)



# A FUCNTION TO CHECK IF A STRING IS PALINDROME
def is_palindrome(s):
    s = s.lower().replace(' ', '')
    return s ==s [::-1]


print(is_palindrome('A man a plan a canal Panama '))
print(is_palindrome('HALLO'))


# CALCULATE THE FACTORIALS OF A NUMBER USING RECURSION
def factorial(n):
    if n == 0:
        return 1
    else:
        n * factorial(n-1)
        
# A FUNCTION TO READ A FILE AND COUNT THE FREQUENCY OF EACH WORD

def count_word_frequency(file_path):
    word_count = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower().strip('.,!?;:,"\'')
                word_count[word] = word_count.get(word, 0) + 1
    return word_count




    