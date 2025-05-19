from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operator = request.form['operator']

        if operator == 'sumar':
            result = num1 + num2
        elif operator == 'restar':
            result = num1 - num2
        elif operator == 'multiplicar':
            result = num1 * num2
        elif operator == 'dividir':
            if num2 != 0:
                result = num1 / num2
            else:
                result = 'Error: División por cero'
        else:
            result = 'Error: Operador inválido'
    except Exception as e:
        result = f'Error: {e}'

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
