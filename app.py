from flask import Flask

app = Flask(__name__)

@app.route('/<name>')
def greet(name):
    return f'hello {name}'

if __name__ == '__main__':
    app.run(debug=True)