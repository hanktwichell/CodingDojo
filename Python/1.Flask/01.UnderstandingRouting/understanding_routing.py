from genericpath import exists
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/success')
def success():
    return "success"

@app.route('/say/<string:word>')
def say_hi(word):
    return f"Hi {word.capitalize()}!"

@app.route('/repeat/<int:times>/<string:word>')
def repeat(times, word):
    result = ""
    for i in range(0,times):
        print(word)
        result += f"<p>{word}</p>"
    return result

@app.route('/<val>')
def no_response(val):
    if len(val) >= 1:
    # if not val == "dojo" or not val == "success" or not val == "say" or not val == "repeat":
        return "Sorry! No Response. Try again."
    return "What?!?"

if __name__ == "__main__":
    app.run(debug=True)
