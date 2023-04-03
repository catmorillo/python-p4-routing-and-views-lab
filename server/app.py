#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:hello>')   
def print_string(hello):
        print(hello)
        return hello

@app.route('/count/<int:num>')
def count(num):
    count = f''
    for n in range(num):
        count += f'{n}\n'
        return count 


#  +, -, *, div
@app.route('/math/<int:num1><string:operation><int:num2>')
def math(num1, num2, operation):
    if operation == '+':
        return str(num1 + num2)

    elif operation == '-':
        return str(num1 - num2)

    elif operation == '*':
        return str (num1 * num2)

    elif operation == 'div':
        return str (num1 / num2)

    elif operation == '%':
        return (num1 % num2)


#return 'Operation not recognized. Please use one of the following: + - * div %'

if __name__ == '__main__':
    app.run(port=5555)