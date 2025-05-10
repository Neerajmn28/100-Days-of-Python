from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before
        function()
        function()
        # Do something after
    return wrapper_function

@delay_decorator
def say_hello():
    print('Hello')
    
@delay_decorator
def say_bye():
    print('Hello')
    
@delay_decorator
def say_greeting():
    
