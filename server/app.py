from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_route(parameter):
    print(parameter)
    return parameter


@app.route('/count/<int:parameter>')
def count_route(parameter):
    count = ''
    for i in range(parameter):
        count += str(i) + '\n'
    return count

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math_route(num1, operation, num2):
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == 'div':
        if num2!= 0:
            return str(num1 / num2)
        else:
            return 'Error: Division by zero'
    elif operation == '%':
        if num2!= 0:
            return str(num1 % num2)
        else:
            return 'Error: Division by zero'

if __name__ == '__main__':
    app.run()