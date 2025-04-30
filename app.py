from flask import Flask

app = Flask(__name__)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return "Error: el número debe ser mayor o igual a cero"
    else:
        resultado = 1
        for i in range(2, n+1):
            resultado *= i
        return resultado

@app.route('/factorial/<int:numero>')
def mostrar_factorial(numero):
    resultado = factorial(numero)
    return f'El factorial de {numero} es {resultado}'

if __name__ == '__main__':
    app.run(debug=True)
