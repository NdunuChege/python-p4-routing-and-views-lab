from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string>')
def print_string(string):
    print(string)  # Prints to console
    return string  # Displays in browser

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = range(parameter)
    return '\n'.join(str(num) for num in numbers) + '\n'  # Added extra \n at the end

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return "Cannot divide by zero"
        result = num1 / num2
    elif operation == '%':
        if num2 == 0:
            return "Cannot perform modulo with zero"
        result = num1 % num2
    else:
        return "Invalid operation"
    
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)