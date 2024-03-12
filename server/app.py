#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string>')
def print_string(string):
    print (string)
    return string

@app.route('/count/<int:parameter>')
def count(parameter):
    number_list = "\n".join(str(number) for number in range (0, parameter)) + "\n"
    print(number_list)
    return number_list


@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        'div': lambda x, y: x / y if y != 0 else 'Error: Division by zero',
        '%': lambda x, y: x % y,
    }
       
    result = operations[operation](num1, num2)  
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
